# 创建list：list是一种有序的集合，可以随时添加和删除其中的元素。
L = ['lxw', 24, 'M', 'zfr', 23, 'W']
print(L)

# 身份标识--判断是不是一个列表，打印输出true或者false
print(type(L) is list)

# 遍历List，注意越界情况
print("姓名：", L[0], " 年龄：", L[1], " 性别：", L[2])
print("姓名：", L[3], " 年龄：", L[4], " 性别：", L[5])

# 倒序输出list,-1代表倒数第一个，-2代表倒数第二个，以此类推
print(L[-1])

# append添加元素，默认添加到最后一位
L.append('hello')
print('append后的元素', L)

# insert添加元素，可以指定相应的位置添加,list的元素是从0开始数起
L.insert(0, "对象")
print('insert后的元素', L)

# list删除元素，注意删除后的各个元素位置，连续删除时要注意删除一个元素后它的元素位置的改变
L.pop(0)
print("删除后的list：", L)
print("删除的值为：", L.pop(0))

# pop内不添加数字默认是删除最后一个元素
L.pop()
print("删除后的list：", L)

# 替换两个元素,先找到两个需要替换的元素位置
L[-1] = 'M'
L[2] = 'W'
print("替换后的元素：", L)

# 切片替换多个元素
L[2:4] = {"A", "B"}
print("切片替换后的元素：", L)

# 删除元素
L.remove(L[2])
print("remove后的list：", L)

# 删除元素
del L[0]
print("del后的元素", L)

# 清空列表
L.clear()
print(L)

