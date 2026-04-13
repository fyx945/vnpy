@ECHO OFF
ECHO ========================================
ECHO AI量化软件 PyInstaller Build Script
ECHO ========================================
ECHO.

:: Check PyInstaller
python -c "import PyInstaller" 2>/dev/null
IF ERRORLEVEL 1 (
    ECHO PyInstaller not installed, installing...
    pip install pyinstaller
)

ECHO.
ECHO Building...
ECHO.

:: Build with PyInstaller
pyinstaller app.spec --clean

ECHO.
ECHO ========================================
ECHO Build Complete!
ECHO Output: dist\AIQuantSoftware
ECHO ========================================
PAUSE
