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
uv run git_pull
call "%cd%\devLP\src\devlp\start_internet_LP\start_internet.bat"
call  "%cd%\devLP\src\devlp\start_explorer_LP\start_explorer.bat"
call  "%cd%\devLP\src\devlp\start_pythonLP_LP\start_pythonLP.bat"
pause