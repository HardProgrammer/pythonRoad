# 函数高阶  

import math;

def fiter_func(x):
    r = int(math.sqrt(x))
    return r * r == x

# 过滤获取1，101中该数的平方为1-100内的数字
fiter_return = filter(fiter_func,range(1,101))

print(list(fiter_return))

# 匿名函数--lambda关键字
map_return_value = map(lambda x:x * x,[1,2,3,4,5])
print(list(map_return_value))

