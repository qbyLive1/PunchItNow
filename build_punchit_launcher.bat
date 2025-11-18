@echo off
echo ========================================
echo   Building PunchIT Launcher.exe
echo ========================================
echo.

REM Check if PyInstaller is installed
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo [1/3] Installing PyInstaller...
    pip install pyinstaller
) else (
    echo [1/3] PyInstaller already installed
)

echo.
echo [2/3] Building launcher.exe...
pyinstaller --onefile --noconsole --name "PunchIT Launcher" launcher.py

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Build failed!
    pause
    exit /b 1
)

echo.
echo [3/3] Copying to release folder...
if not exist release mkdir release
copy dist\"PunchIT Launcher.exe" release\
copy "New soft 3.0.py" release\
copy conversion_monitor.py release\
copy version.json release\

echo.
echo ========================================
echo   BUILD SUCCESSFUL!
echo ========================================
echo.
echo Files ready in: release\
echo   - PunchIT Launcher.exe
echo   - New soft 3.0.py
echo   - conversion_monitor.py  
echo   - version.json
echo.
echo Now push to GitHub:
echo   git add .
echo   git commit -m "Update v3.0.1"
echo   git push
echo.
pause
