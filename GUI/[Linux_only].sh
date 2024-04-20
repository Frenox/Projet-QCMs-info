#!/bin/bash


echo "Lancement du serveur Flask..."
python3 Website/app.py &


sleep 2


echo "Lancement du navigateur..."
xdg-open http://127.0.0.1:5000

echo "L'application est maintenant en cours d'exécution dans votre navigateur web."
