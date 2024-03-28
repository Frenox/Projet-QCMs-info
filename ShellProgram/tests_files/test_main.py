import unittest
import subprocess
import os
from pathlib import Path

class TestQCMGeneration(unittest.TestCase):

    def setUp(self):
        # Chemin relatif vers le dossier contenant les fichiers de code et de réponse
        self.base_dir = Path(__file__).parent.parent
        self.code_files_path = self.base_dir / "tests_files/Codefiles"
        self.answer_files_path = self.base_dir / "tests_files/answerFile"
        # Chemin relatif du script à tester
        self.script_path = self.base_dir / "main.py"
        # Chemin relatif vers le répertoire de sortie
        self.output_dir = self.base_dir / "Outputs"

        # S'assurer que le répertoire de sortie existe
        self.output_dir.mkdir(exist_ok=True)

    def test_generation(self):
        # Liste tous les fichiers de code dans le dossier spécifié
        code_files = os.listdir(self.code_files_path)
        
        for code_file in code_files:
            # Construit le chemin vers le fichier de réponse associé
            answer_file = self.answer_files_path / code_file.replace("codeFile", "answersFile")
            
            # Construit la commande à exécuter
            command = f"python {self.script_path} amc python3 {self.code_files_path / code_file} {answer_file}"
            
            # Exécute le script avec les arguments appropriés
            subprocess.run(command, shell=True, check=True)
            
            # Vérifie si les fichiers de sortie attendus ont été générés
            # Ajuster la logique de vérification en fonction de la manière dont votre script nomme ses fichiers de sortie.
            # Par exemple:
            output_files = os.listdir(self.output_dir)
            # Cette partie du code doit être ajustée selon le nom exact des fichiers générés
            # self.assertIn("nom_du_fichier_attendu", output_files)

    def tearDown(self):
        # Nettoyer les fichiers de sortie après chaque test si nécessaire
        pass

if __name__ == '__main__':
    unittest.main()
