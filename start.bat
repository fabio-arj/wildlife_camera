@echo off
title Iniciando o Reader...
echo ============================================
echo      Inicializando o aplicativo Reader
echo ============================================
echo.

where uv >nul 2>nul
if %errorlevel% neq 0 (
    echo O UV não foi encontrado. Baixando o instalador...
    powershell -Command "Invoke-WebRequest https://astral.sh/uv/install.ps1 -UseBasicParsing | Invoke-Expression"
)

echo.
echo Configurando ambiente...
uv sync

echo.
echo Iniciando o aplicativo...
start "" uv run python app.py
exit
