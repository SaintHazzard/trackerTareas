@echo off
:: Script para activar el entorno virtual y instalar dependencias

:: Comprueba si Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python no está instalado. Por favor, instálalo antes de continuar.
    exit /b
)

:: Crea un entorno virtual si no existe
if not exist "venv" (
    echo Creando el entorno virtual...
    python -m venv env
)

:: Activa el entorno virtual
call venv\Scripts\activate.bat

:: Comprueba si requirements.txt existe
if not exist "requirements.txt" (
    echo No se encontró el archivo requirements.txt.
    echo Crea el archivo con las dependencias necesarias y vuelve a ejecutar el script.
    exit /b
)

:: Instala las dependencias
pip install --upgrade pip
pip install -r requirements.txt

:: Confirma que las dependencias fueron instaladas
echo Dependencias instaladas correctamente.

echo El entorno está listo. Para desactivarlo, usa el comando "deactivate".
exit