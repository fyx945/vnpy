# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files, collect_submodules

block_cipher = None

# 收集所有 vnpy 子模块
hiddenimports = [
    'vnpy',
    'vnpy.trader',
    'vnpy.event',
    'vnpy.chart',
    'vnpy.alpha',
    'vnpy.rpc',
    'vnpy_ctp',
    'vnpy_ctastrategy',
    'vnpy_ctabacktester',
    'vnpy_datamanager',
]

# 收集所有子模块
for mod in [
    'vnpy.trader',
    'vnpy.event',
    'vnpy.chart',
    'vnpy.alpha',
    'vnpy.rpc',
]:
    hiddenimports.extend(collect_submodules(mod))

# 收集 PySide6 资源
from PyInstaller.utils.hooks import collect_all
pyside6_data = collect_data_files('PySide6')
pyside6_data.extend(collect_data_files('shiboken6'))

a = Analysis(
    ['examples/veighna_trader/run.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('vnpy/trader/locale', 'vnpy/trader/locale'),
        ('vnpy/trader/ui/ui', 'vnpy/trader/ui/ui'),
    ],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'matplotlib',
        'PyQt5',
        'PyQt6',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure_a, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    *pyside6_data,
    name='AI量化软件',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # GUI程序，设为True会显示黑窗口
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # 可设置: icon='app.ico'
)
