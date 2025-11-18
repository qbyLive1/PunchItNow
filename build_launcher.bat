@echo off
echo ========================================
echo   Building Conversion Monitor Launcher
echo ========================================
echo.

REM Перевірка PyInstaller
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo [ERROR] PyInstaller not found!
    echo Installing PyInstaller...
    pip install pyinstaller
)

echo [1/3] Cleaning old builds...
if exist "build" rmdir /s /q build
if exist "dist" rmdir /s /q dist
if exist "*.spec" del /q *.spec

echo [2/3] Building launcher.exe...
pyinstaller --onefile --windowed --name="ConversionMonitorLauncher" launcher.py

echo [3/3] Copying resources...
if exist "dist\ConversionMonitorLauncher.exe" (
    echo.
    echo ========================================
    echo   BUILD SUCCESSFUL!
    echo ========================================
    echo.
    echo EXE Location: dist\ConversionMonitorLauncher.exe
    echo Size: 
    dir "dist\ConversionMonitorLauncher.exe" | findstr "ConversionMonitorLauncher.exe"
    echo.
    echo Next steps:
    echo 1. Upload conversion_monitor.py to GitHub/Server
    echo 2. Upload version.json to GitHub/Server  
    echo 3. Update URLs in launcher.py
    echo 4. Rebuild and distribute!
    echo.
) else (
    echo.
    echo [ERROR] Build failed! Check errors above.
    echo.
)

pause
