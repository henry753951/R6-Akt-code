# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['output.py', 'G:\\Users\\Henry\\Desktop\\Python\\R6 Akt code'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [('white-settings-icon-0.jpg','G:\\Users\\Henry\\Desktop\\Python\\R6 Akt code\\white-settings-icon-0.jpg','DATA'),('icon.ico','G:\\Users\\Henry\\Desktop\\Python\\R6 Akt code\\icon.ico','DATA')],
          name='r6中文輸入工具',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='icon.ico')
