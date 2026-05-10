# Original work by CorpNewt (2019)
# Modifications and .exe packaging by Disaster work (2026)
# -*- mode: python ; coding: utf-8 -*-
# ProperTree PyInstaller spec file
# Builds a windowed (no console) one-dir bundle

import os

block_cipher = None

# Paths
BASE_DIR = os.path.abspath('.')
SCRIPTS_DIR = os.path.join(BASE_DIR, 'Scripts')

# Data files to bundle (source, destination_folder)
datas = [
    (os.path.join(SCRIPTS_DIR, 'menu.plist'),      'Scripts'),
    (os.path.join(SCRIPTS_DIR, 'snapshot.plist'),   'Scripts'),
    (os.path.join(SCRIPTS_DIR, 'version.json'),     'Scripts'),
    (os.path.join(SCRIPTS_DIR, 'shortcut.ico'),     'Scripts'),
    (os.path.join(SCRIPTS_DIR, 'shortcut.icns'),    'Scripts'),
    (os.path.join(SCRIPTS_DIR, 'update_check.py'),  'Scripts'),
]

a = Analysis(
    ['ProperTree.py'],
    pathex=[BASE_DIR],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'Scripts',
        'Scripts.plist',
        'Scripts.plistwindow',
        'Scripts.downloader',
        'Scripts.config_tex_info',
        'Scripts.utils',
        'tkinter',
        'tkinter.ttk',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'tkinter.font',
        'tkinter.colorchooser',
        'plistlib',
        'multiprocessing',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='ProperTree',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,         # Windowed mode — no console window
    icon=os.path.join(SCRIPTS_DIR, 'shortcut.ico'),
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='ProperTree',
)
