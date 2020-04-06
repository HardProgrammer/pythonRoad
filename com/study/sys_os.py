'''
    系统相关模块
'''

import sys
import os

# 打印python的环境变量
print(sys.path)

# 打印当前文件的绝对路径
print(sys.argv)

# 模拟cmd--只执行命令不保存结果
os.system("dir")


# 模拟cmd--保存结果
print(os.popen("dir").read())