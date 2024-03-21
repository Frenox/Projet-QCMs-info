@echo off
:: Vérifier si exécuté en tant qu'administrateur
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Exécuté avec des droits d'administrateur.
) else (
    echo Ce script doit être exécuté en tant qu'administrateur.
    exit /b
)

:: Activer WSL
echo Activation de WSL...
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

:: Activer la plate-forme de machine virtuelle (pour WSL 2)
echo Activation de la plate-forme de machine virtuelle...
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

:: Télécharger la mise à jour du noyau Linux pour WSL 2 (ajustez le lien si nécessaire)
echo Téléchargement de la mise à jour du noyau Linux pour WSL 2...
powershell -command "Invoke-WebRequest -Uri https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi -OutFile %TEMP%\wsl_update_x64.msi"

:: Installer la mise à jour du noyau Linux
echo Installation de la mise à jour du noyau Linux pour WSL 2...
msiexec /i %TEMP%\wsl_update_x64.msi /quiet

:: Configurer WSL 2 comme version par défaut
echo Configuration de WSL 2 comme version par défaut...
wsl --set-default-version 2

echo Installation terminée. Redémarrez votre ordinateur pour appliquer les modifications.
