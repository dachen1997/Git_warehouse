import os
'''
os.path.abspath(__file__)   获取当前文件的位置的绝对路径
os.path.dirname(path)       获取指定路径的上层路径

'''

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#获取到项目根目录

ALLpy_PATH = os.path.join(BASE_PATH,'all.py')

TmpDir_PATH = os.path.join(BASE_PATH,'Tmp')

Report_PATH = os.path.join(BASE_PATH,'Report')

DataDir_PATH = os.path.join(BASE_PATH,'Data')
