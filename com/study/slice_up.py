# 切片相关知识

# 创建一个学生名的list
studentName = ["张三", "李四", "王五", "赵六", "小七"]
# 打印输出该list
print(studentName)

print(studentName[0:5])

# 从第二个开始到最后一个打印
print(studentName[1:])

# 从第一个开始到第三个
print(studentName[0:3])

# 从第二个取到倒数第三个
print(studentName[1:-2])

# 从第二个到最后一个每隔一个取一个数（第三位为正表示从左往右间隔，为负表示从右往左间隔）
print(studentName[1::2])

# 从第二个到第四个每隔一个取一个数
print(studentName[1:3:2])

# 从第二个到最后一个从右往左每隔一个取一个数
print(studentName[2::-2])

# 从倒数第二个开始从左往右到最后一个
print(studentName[-2::])

# 定义一个list
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 利用切片获取前5个数
print(L[0:5])
print(L[:5])

# 获取3的倍数:从第二个数开始每隔3个去一个数
print(L[2::3])

# 获取倒数3个数
print(L[-3:])
