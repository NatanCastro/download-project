# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['gui.py'],
    pathex=['/home/natan/workspace/download-project'],
    binaries=[],
    datas=[
#        ('/path/to/your/datafile1', 'dest/folder1'),
#        ('/path/to/your/datafile2', 'dest/folder2')
    ],
    hiddenimports=[
        'requests',
        'instaloader',
        'pytube',
        'tkinter'
    ],
    hookspath=['./hoooks'],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main'
)
