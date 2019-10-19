# for循环打印字符
for letter in "python":
    print("打印字符：", letter)

# 定义一个list
names = ["lxw", "测试", "liu"]

# for循环打印list
for test in names:
    print("打印list：", test)

# 遍历一个tuple并将里面的元素相加
t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
sum = 0
for t1 in t:
    sum += t1
print(sum)

# for嵌套输出十位数小于个位数（100以内）的数
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for y in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if x < y:
            print(x * 10 + y)

# for循环打印99乘法表
for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for j in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if i <= j:
            print(i, "*", j, "=", i * j)

# 左三角形打印乘法表
for i in range(1, 10):
    for j in range(i, 10):
        print("%d*%d=%2d" % (i, j, i * j), end=" ")
    print("")

# 左下三角形打印乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%2d" % (i, j, i * j), end=" ")
    print("")
