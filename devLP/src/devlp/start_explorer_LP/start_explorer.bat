@echo off
setlocal enabledelayedexpansion

rem Get current path to .bat
set "CURRENT_DIR=%~dp0"
rem Remove final backslash
set "CURRENT_DIR=%CURRENT_DIR:~0,-1%"

:loop
rem Check if current folder is called pythonLP
for %%I in ("%CURRENT_DIR%") do set "DIRNAME=%%~nxI"

if /i "%DIRNAME%"=="pythonLP" (
    cd /d "%CURRENT_DIR%"
    goto run_script
) else (
    rem Check parent
    for %%I in ("%CURRENT_DIR%\..") do set "CURRENT_DIR=%%~fI"
    rem Exit if arrived to root
    if "%CURRENT_DIR%"=="%CURRENT_DIR%\.." (
        echo Folder pythonLP not found
        exit /b 1
    )
    goto loop
)

:run_script
start explorer
timeout /t 2 /nobreak >nul
nircmd clipboard set "pythonLP"
nircmd sendkeypress alt+d
nircmd wait 100
nircmd sendkeypress ctrl+v
nircmd wait 100
nircmd sendkeypress enter
nircmd wait 100

nircmd sendkeypress ctrl+t
nircmd wait 500
nircmd clipboard set "pythonLP/libsLP"
nircmd sendkeypress alt+d
nircmd wait 100
nircmd sendkeypress ctrl+v
nircmd wait 100
nircmd sendkeypress enter
nircmd wait 100

nircmd sendkeypress ctrl+t
nircmd wait 500
nircmd clipboard set "pythonLP/devLP/.links"
nircmd sendkeypress alt+d
nircmd wait 100
nircmd sendkeypress ctrl+v
nircmd wait 100
nircmd sendkeypress enter
nircmd wait 100

nircmd sendkeypress ctrl+t
nircmd wait 500
nircmd clipboard set "pythonLP/.debug"
nircmd sendkeypress alt+d
nircmd wait 100
nircmd sendkeypress ctrl+v
nircmd wait 100
nircmd sendkeypress enter
nircmd wait 100

nircmd sendkeypress ctrl+t
nircmd clipboard set ""
nircmd win min ititle "Explor"