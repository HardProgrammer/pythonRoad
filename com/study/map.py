# map用于接收参数是List的函数，方便遍历参数里面的元素
def f(x):
    return x * x


# 使用map对函数进行输出,python3要用list去接收才可以进行正常输出
print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


# 函数实现第一个字母大小，其他字母小写
def toUpper(x):
    return x[0].upper() + x[1:].lower()

print(list(map(toUpper, ["LXW", "liSa", "hello"])))
