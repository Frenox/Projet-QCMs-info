import docker
import os
import tempfile
from donneesJSON import *

# Configuration des langages avec modèle de commande inclus
lang_config = getKnownLanguages()

def execution_docker(code, language_key):
    if language_key not in lang_config:
        raise ValueError("Langage non configuré")

    extension, docker_image, command_template = lang_config[language_key]
    filename = f"fichier_test{extension}"

    with tempfile.TemporaryDirectory() as tempdir:
        filepath = os.path.join(tempdir, filename)
        with open(filepath, "w") as file:
            file.write(code)

        volume_path = "/app"
        command = command_template.format(filename=filename)

        client = docker.from_env()
        logs = ""
        try:
            container = client.containers.run(
                docker_image, command,
                volumes={tempdir: {'bind': volume_path, 'mode': 'rw'}},
                working_dir=volume_path, detach=True,
                stdout=True, stderr=True
            )
            container.wait()
            logs = container.logs(stdout=True, stderr=True).decode('utf-8')
        finally:
            if 'container' in locals():
                container.remove(force=True)

    return logs.splitlines()
