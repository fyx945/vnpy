@ECHO OFF
ECHO ========================================
ECHO AI量化软件 PyInstaller 打包脚本
ECHO ========================================
ECHO.

:: 检查 PyInstaller 是否安装
python -c "import PyInstaller" 2>/dev/null
IF ERRORLEVEL 1 (
    ECHO PyInstaller 未安装，正在安装...
    pip install pyinstaller
)

ECHO.
ECHO 开始打包...
ECHO.

:: 打包
pyinstaller app.spec --clean

ECHO.
ECHO ========================================
ECHO 打包完成！
ECHO 输出目录: dist\AI量化软件
ECHO ========================================
PAUSE
