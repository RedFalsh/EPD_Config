#! usr/bin/python
# coding=utf-8

import os

class cxFreeze:
    def runcmd(self):
        path = os.getcwd()
        build = "build"
        bdist_msi = "bdist_msi"
        print(path)
        os.system('python %s\cx_setup.py %s'%(build))

tool = cxFreeze()
tool.runcmd()
# #ui文件转py文件，这里要安装pyuic5
# path_ui = '/home/xiong/PycharmProjects/nt_test/Dialog_Task.ui'
# paty_py = '/home/xiong/PycharmProjects/nt_test/Dialog_Task.py'
# os.system('pyuic5 -o %s %s'%(paty_py,path_ui))