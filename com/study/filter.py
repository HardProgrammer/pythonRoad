import math

# 过滤函数--输出1-100偶数
def is_int(x):
    return x % 2 == 0


# 用list来接收结果集
print(list(filter(is_int, range(1, 101))))


# 判断1-100的平方根是否是整数
def is_sqr(x):
    r = int(math.sqrt(x))
    # 将r强制转化为int型，然后判断它的平方是不是原来的数
    return r * r == x


print(list(filter(is_sqr, range(1, 101))))
