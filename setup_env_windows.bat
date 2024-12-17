@echo off
:: Script para activar el entorno virtual y instalar dependencias

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python no está instalado. Por favor, instálalo antes de continuar.
    exit /b
)

if not exist "venv" (
    echo Creando el entorno virtual...
    python -m venv env
)

call venv\Scripts\activate.bat

if not exist "requirements.txt" (
    echo No se encontró el archivo requirements.txt.
    echo Crea el archivo con las dependencias necesarias y vuelve a ejecutar el script.
    exit /b
)

pip install --upgrade pip
pip install -r requirements.txt

echo Dependencias instaladas correctamente.

echo El entorno está listo. Para desactivarlo, usa el comando "deactivate".
exit