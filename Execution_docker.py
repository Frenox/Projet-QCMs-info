import docker
import os
import uuid

def execution_docker(code, language):
    client = docker.from_env()
    nom_langage, extension = language
    fichier = "fichier_test" + extension
    volume_path = "/app"
    docker_image = ""
    command = ""

    if nom_langage == "python3":
        docker_image = "python:3.8"
        command = f"python {volume_path}/{fichier}"
    elif nom_langage == "python2":
        docker_image = "python:2.7"
        command = f"python {volume_path}/{fichier}"
    elif nom_langage == "c":
        docker_image = "gcc:latest"
        command = f"/bin/bash -c 'gcc {volume_path}/{fichier} -o {volume_path}/{fichier}.out && {volume_path}/{fichier}.out'"
    elif nom_langage == "cpp":
        docker_image = "gcc:latest"
        command = f"/bin/bash -c 'g++ {volume_path}/{fichier} -o {volume_path}/{fichier}.out && {volume_path}/{fichier}.out'"
    elif nom_langage == "java":
        docker_image = "openjdk:latest"
        class_name = "Main"
        command = f"/bin/bash -c 'javac {volume_path}/{fichier} && java -cp {volume_path} {class_name}'"
    elif nom_langage == "javascript":
        docker_image = "node:latest"
        command = f"node {volume_path}/{fichier}"

    # Écriture du fichier
    with open(fichier, "w") as file:
        file.write(code)

    try:
        # Exécution du code dans un conteneur Docker
        container = client.containers.run(docker_image, command, volumes={f"{os.getcwd()}": {'bind': volume_path, 'mode': 'rw'}}, working_dir=volume_path, detach=True, stdout=True, stderr=True)
        response = container.wait()  # Attendre que le conteneur ait terminé
        logs = container.logs(stdout=True, stderr=True)
    finally:
        # Suppression du fichier de code après exécution
        os.remove(fichier)
        # Suppression du conteneur
        container.remove(force=True)

    return logs.decode('utf-8').splitlines()

code_cpp = """
#include <iostream>

int main() {
    std::cout << "Hello from C++" << std::endl;
    return 0;
}
"""

#logs = execution_docker(code_cpp, ["cpp", ".cpp"])
#print(logs)
