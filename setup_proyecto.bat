@echo off

:: Crear la carpeta principal del proyecto
mkdir POS_Polleria_Montiel
cd POS_Polleria_Montiel

:: Crear las subcarpetas para organización
mkdir src
mkdir assets
mkdir tests

:: Inicializar el repositorio Git
git init

:: Crear un archivo .gitignore básico
echo venv/ >> .gitignore
echo *.pyc >> .gitignore
echo __pycache__/ >> .gitignore

:: Crear entorno virtual (opcional)
python -m venv venv

:: Mensaje de confirmación
echo Estructura del proyecto creada con éxito. ¡Listo para comenzar!

:: Instrucciones para activar el entorno virtual
echo Para activar el entorno virtual, usa: venv\Scripts\activate
