# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['Files\\Python38', 'LB_AWS_double.py'],
             pathex=['D:\\Python_workobject\\venv\\Lib\\site-packages', 'D:\\Program', 'C:\\Users\\Lenovo\\Desktop\\aws'],
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
          [],
          name='',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )

pyinstaller -F -w AWS_login1.spec