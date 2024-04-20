@echo off
echo Démarrage du serveur Flask...
start /B python Website\app.py
timeout /T 5 /NOBREAK

echo Ouverture du navigateur web...
start http://127.0.0.1:5000

echo L'application est maintenant en cours d'exécution dans votre navigateur web.
pause
