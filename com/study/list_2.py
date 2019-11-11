'''
    列表表达式：
        使用列表表达式来简化代码
'''

# 生成[1x1, 2x2, 3x3, ..., 10x10]
s = [x * x for x in range(1,11)]

print(s)

# 生成1-10内偶数的平方值列表
s1 = [x * x for x in range(1,11) if x % 2 == 0]
print(s1)


# 两个字符串拼接生成列表
s2 = [x + y for x in "ABC" for y in "XYZ"]
print(s2)