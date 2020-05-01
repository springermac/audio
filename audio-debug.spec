# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['audio-run.py'],
             pathex=['.'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=['PyQt5.QtWebEngine', 'PyQt5.QtWebEngineCore', 'PyQt5.QtWebEngineWidgets', 'PyQt5.QtQuickWidgets', 'PyQt5.QtQuick', 'PyQt5.QtQml', 'PyQt5.QtWebChannel', 'PyQt5.QtQtWebSockets', 'PyQt5.QtWebKit', 'lib2to3'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='audio-debug',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='audio-debug')
app = BUNDLE(coll,
             name='audio-debug.app',
             icon=None,
             bundle_identifier=None,
             info_plist={
                'NSHighResolutionCapable': True
             })
