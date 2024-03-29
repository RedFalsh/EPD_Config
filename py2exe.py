from distutils.core import setup
from PyQt5 import QtCore, QtGui, QtWidgets
import py2exe
import sys
#this allows to run it with a simple double click.
sys.argv.append('py2exe')

py2exe_options = {
        "includes": ["sip"],  # 如果打包文件中有PyQt代码，则这句为必须添加的
        "dll_excludes": ["MSVCP90.dll",],  # 这句必须有，不然打包后的程序运行时会报找不到MSVCP90.dll，如果打包过程中找不到这个文件，请安装相应的库
        "compressed": 1,
        "optimize": 2,
        "ascii": 0,
        "bundle_files": 1,  # 关于这个参数请看第三部分中的问题(2)
        }

setup(
      name = 'PyQt Demo',
      version = '1.0',
      windows =[{"script": "Config_main.py", "icon_resources": [(1, "app.ico")] }],
      # windows = ['Config_main.py',{"icon_resoureces": [(1, r'F:\Python\Git\EPD_Config\app.ico')]}],   # 括号中更改为你要打包的代码文件名
      data_files=[
          ("",
                   [r"F:\Python\python34\Lib\site-packages\PyQt5\libEGL.dll"]),
                  ("platforms",
                   [r"F:\Python\python34\Lib\site-packages\PyQt5\plugins\platforms\qwindows.dll"])],

      zipfile = None,
      options = {'py2exe': py2exe_options}
      )