
import os
import sys
import py2exe
from distutils.core import setup

origIsSystemDLL = py2exe.build_exe.isSystemDLL
def isSystemDLL(pathname):
    dlls = ("libfreetype-6.dll", "libogg-0.dll", "sdl_ttf.dll")
    if os.path.basename(pathname).lower() in dlls:
        return 0
    return origIsSystemDLL(pathname)
py2exe.build_exe.isSystemDLL = isSystemDLL

sys.argv.append('py2exe')
setup(options={'py2exe': {'bundle_files': 1, 'compressed': True}},
      windows=[{'script': "game.py"}],
      zipfile=None)
