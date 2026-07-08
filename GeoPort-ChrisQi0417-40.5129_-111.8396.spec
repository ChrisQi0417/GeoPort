# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import copy_metadata

datas = [('src\\templates', 'templates'), ('src\\templates', 'src\\templates'), ('CURRENT_VERSION', '.'), ('BROADCAST', '.'), ('.venv\\Lib\\site-packages\\pytun_pmd3\\wintun', 'pytun_pmd3\\wintun')]
datas += copy_metadata('readchar')
datas += copy_metadata('inquirer3')
datas += copy_metadata('pymobiledevice3')
datas += copy_metadata('sslpsk-pmd3')
datas += copy_metadata('pyimg4')
datas += copy_metadata('pytun-pmd3')


a = Analysis(
    ['src\\main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='GeoPort-ChrisQi0417-40.5129_-111.8396',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    uac_admin=True,
)
