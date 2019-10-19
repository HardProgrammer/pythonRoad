'''
输出语句
 print()

注释:
    单行注释 用#
	多行注释用三个单引号或三个双引号 ''''''

缩进:
    tab键和4个空格不相等。
    windows和linux系统的tab键不相同。
'''

# 输出语句
print("Hello World！")

# 定义一个变量
name = "lxw"

# 添加end可以不进行换行
print("中文name:", end="")
print(name)

# 换行，等价于print(end="\n")
print()

# 使用逗号也可以不换行
print("name:", name)

# 短路法则--如果该变量为空，就输出or后面的字符串
test_name = 'python'
print('hello,', test_name or 'world')

# 因为Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True
string_name = ''
# 后面的判断为false，因此只输出前面的字符串
print('hello,', string_name and 'world')
print('test,', string_name or 'world')

# 转义字符
print("I\'m from China.My name is \'liu\'")

# 不需要转义字符
print(r'''He says:"My name is liu."''')

# \n表示换行
print("I\'m from China.\n I love you!")

# 逗号会自动拼接
print("Age = ", 12)

# print("Age = " + 12) 字符串和整型不能直接相加，必须通过str(整型)进行转换才能相加
print("Age = " + str(12))

'''测试注释 (多行注释)'''
