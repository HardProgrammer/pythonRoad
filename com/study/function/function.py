'''
    函数：
        1、减少重复代码；
        2、方便修改，便于拓展；
        3、保持代码一致性；
    函数的返回值：
        1、如果没有return默认返回为null
        2、如果返回多个对象，会封装成一个元组返回
'''

import math
import time

# 获取当前时间
time_fomat = "%Y-%m-%d %X"
nowTime = time.strftime(time_fomat)
print("现在时间是：", nowTime)


# 定义一个求和函数
def sum(a, b):
    print(a + b)


sum(3, 4)


# 带默认参数的函数
def getName(name="lxw"):
    print("hello,", name)


getName()
getName("liu")


# 参数是可变函数：可变参数 args 是一个tuple，当0个参数传入时，args是一个空tuple。
def average(*args):
    sum = 0.0
    # 如果没有参数就返回0
    if len(args) == 0:
        return sum
    for x in args:
        sum = sum + x
    return sum / len(args)


# 这里对浮点数有进行处理
print(average())
print(average(1, 2))
print(average(1, 2, 2, 3, 4))

# 变量指向函数
z = abs
print(z(-21))


# 实现两个数的绝对值相加
def add(x, y, f):
    return f(x) + f(y)


print(add(2, -4, abs))


# 字符串大小写转化
def upperStr(s):
    return s.upper()


# 对第一个字母进行大写转化--使用切片
def upperStr1(s):
    return s[0].upper() + s[1:]


print(upperStr("hello"))
print(upperStr1("hello"))


# 返回不同类型的值
def fans():
    return 1, "33", "测试", [1, 2, 3]


print(fans())
