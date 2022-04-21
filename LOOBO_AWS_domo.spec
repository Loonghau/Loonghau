# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['LOOBO_AWS_domo.py','zmcwrapper.py','temperature.py'],
             pathex=['C:\\Users\\Lenovo\\.virtualenvs\\Lenovo-ezd1lI9Y\\lib\\site-packages', 'C:\\Users\\Lenovo\\Desktop\\aws'],
             binaries=[],
             datas=[('C:\\Users\\Lenovo\\Desktop\\aws\\zauxdll.dll','.'),
            ('C:\\Users\\Lenovo\\Desktop\\aws\\zmotion.dll','.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='LOOBO_AWS_domo',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
