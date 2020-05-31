# 1、把函数作为参数

import math
from functools import reduce


def function_add(x, y, f):
    return f(x) + f(y)


# 求两个数的绝对值的和
add = function_add(1, -1, abs)

print(add)

# 求两个数的开根之和
sqrt = function_add(4, 9, math.sqrt)

print(sqrt)

# 2、内置高阶函数


def f(x):
    return x*x


map_return = map(f, [1, 2, 3, 4, 5, 6, 7])
# Python 3.x 返回迭代器,而2.x中会返回列表，所以要进行转化为列表
print(map_return)
print(list(map_return))

# eg: 实现首字母大写，其他小写


def function_toUpCase(x):
    return x[0].upper() + x[1:].lower()


upcase_return = map(function_toUpCase, ["hello", "world"])

print(list(upcase_return))


# 3、reduce()对list的每个元素反复调用函数f，并返回最终结果值。
def function_mul(x, y):
    return x * y


reduce_return = reduce(function_mul, [1, 2, 4, 6, 7])

print(reduce_return)

# reduce实现1+2+3+ ...100


def add(x, y):
    return x + y


add_reduce_return = reduce(add, range(1, 101))

print(add_reduce_return)

# 函数高阶


def fiter_funca(x):
    r = int(math.sqrt(x))
    return r * r == x


# 过滤获取1，101中该数的平方为1-100内的数字
fiter_return = filter(fiter_funca, range(1, 101))

print(list(fiter_return))

# 匿名函数--lambda关键字
map_return_value = map(lambda x: x * x, [1, 2, 3, 4, 5])
print(list(map_return_value))


def addTest():
    print("这是一个参数")

# 将函数作为参数进行传递
def fucTest(func):
    print("打印测试")
    # 高阶函数，不能修改func的源代码
    return func

# 先执行addTest，再执行之前的打印信息
fucTest(addTest())

# 没有执行addTest的打印信息
print(fucTest(addTest))