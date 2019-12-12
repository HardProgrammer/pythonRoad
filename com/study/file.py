'''
文件操作：
    三种基本的操作模式 r(只可读) w（只可写） a（追加）
    流程：1 创建文件对象 2 调用文件方法进行操作  3 关闭文件
'''
f = open('../test/test.text', 'r', encoding="utf-8")
# 获取文件数据
# data = f.read()
# 获取一个字符
date_line = f.read(1)
# print(data)
print(date_line)
