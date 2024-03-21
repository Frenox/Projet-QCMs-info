import docker
import os
import uuid

def execution_docker(code, language):
    client = docker.from_env()
    
    nom_langage, extension = language[:2]  # Présume que les deux premiers éléments sont présents
    fichier = "fichier_test" + extension
    volume_path = "/app"
    docker_image = ""
    command = ""
    container = None  # Initialiser à None pour la gestion dans finally

    # Configuration basée sur le langage
    # [Votre logique ici, similaire à ce que vous avez déjà]

    # Écriture du fichier
    with open(fichier, "w") as file:
        file.write(code)

    try:
        # Exécution du code dans un conteneur Docker
        container = client.containers.run(docker_image, command, volumes={f"{os.getcwd()}": {'bind': volume_path, 'mode': 'rw'}}, working_dir=volume_path, detach=True, stdout=True, stderr=True)
        response = container.wait()  # Attendre que le conteneur ait terminé
        logs = container.logs(stdout=True, stderr=True)
    finally:
        if os.path.exists(fichier):
            os.remove(fichier)
        if container is not None:
            container.remove(force=True)

    return logs.decode('utf-8').splitlines()