# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['AWS_login.py','call_aws.py','zmcwrapper.py','UI_aws_date.py','UI_aws_help.py','UI_aws_logo.py','UI_aws_loobo.py','UI_aws_mac.py','UI_aws_main.py','UI_limit_mac.py','UI_limit_yj.py','UI_new_object.py','UI_position_set.py','UI_system_set.py','temp_set.py',],
             pathex=['C:\\Users\\Lenovo\\.virtualenvs\\Lenovo-ezd1lI9Y\\lib\\site-packages','D:\\Main_project\\aws'],
             binaries=[],
             datas=[('D:\\Main_project\\aws\\zauxdll.dll','.'),
            ('D:\\Main_project\\aws\\zmotion.dll','.')],
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
          name='LB_AWS',
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
          entitlements_file=None, icon='aws.ico' )
