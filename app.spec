# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_data_files, collect_submodules
import os

block_cipher = None

# 收集 vnpy 核心模块 (不包含需要编译的CTP等)
hiddenimports = [
    'vnpy',
]

# 收集所有子模块
for mod in ['vnpy.trader', 'vnpy.event', 'vnpy.chart', 'vnpy.alpha', 'vnpy.rpc']:
    try:
        hiddenimports.extend(collect_submodules(mod))
    except:
        pass

# 添加策略和回测相关模块
hiddenimports.extend([
    'vnpy.trader',
    'vnpy.event', 
    'vnpy.chart',
    'vnpy.alpha',
    'vnpy.rpc',
    'vnpy_ctastrategy',
    'vnpy_ctabacktester',
    'vnpy_datamanager',
])

# 收集 PySide6 资源
pyside6_data = []
try:
    pyside6_data = collect_data_files('PySide6')
    pyside6_data.extend(collect_data_files('shiboken6'))
except:
    pass

# 入口脚本
entry_script = 'examples/veighna_trader/run.py'
if not os.path.exists(entry_script):
    entry_script = 'run.py'

a = Analysis(
    [entry_script],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'matplotlib',
        'PyQt5',
        'PyQt6',
        'torch',
        'tensorflow',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure_a, a.zipped_data, cipher=block_cipher)

exe_args = [
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
]
exe_args.extend(pyside6_data)

exe = EXE(
    *exe_args,
    name='AIQuantSoftware',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)
