# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['calendar-bot.py'],
             pathex=['C:\\Users\\Victor\\OneDrive\\Desktop\\CS\\PythonProject\\Gym Scheduler'],
             binaries=[],
             datas=[("credentials-calendar.json", "."), ("credentials.json", "."), ("gmail.py", "."),
             ("C:\Python38\Lib\site-packages\google_api_python_client-1.11.0.dist-info/*", "google_api_python_client-1.11.0.dist-info")],
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
          name='calendar-bot',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True)
