'''
    函数传参
        1.实参和形参
        2.参数默认值
        3.多参数传递
'''


# 函数里的参数代表的是形式参数，而调用的是时候传来的参数为实际参数
def add(a, b):
    return a + b


print(add(1, 2))


# 设定默认参数进行返回
def adds(a=5, b=2):
    return a + b


print(adds())
print(adds(3))  # 结果是3+2


# 单个默认参数设置
def print_info(name, age=5):
    return "hello " + name + ":age=" + str(age)


print(print_info("lxw"))


# 输出键值对，形式参数为**kwargs，该参数会接收键值对，并且只能放在最后面
def key_value(**kwargs):
    return kwargs


print(key_value(job='IT'))


# 多参数传值：不定参数，必须放在键值对不定参数前面，默认参数往左放
def addsAll(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(addsAll(1, 2, 3, 4))
