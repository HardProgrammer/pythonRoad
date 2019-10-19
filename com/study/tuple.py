'''
    元组：不可变类型
'''

# tuple是另一种有序的列表，中文翻译为“ 元组 ”。tuple一旦创建完毕，就不能修改了。
t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# 元素是用（）来包起来的
print("tuple:", t)

# 主要单元素和tuple中的一个元素的创建区别
t1 = (1)
# 会输出整数1
print("t1:", t1)  

t2 = (1,)
print("t2:", t2)

# tuple是不可变的，但是如果元素中是一个list就不一样了
tl = ('aa', 'bb', ['cc', 'dd'])
print("包含list的tuple：", tl)

T = tl[2]
print("tuple里面的list：", T)

T[0] = "ll"
T[1] = "xx"
print("改变list的tuple：", tl)

# tuple包含tuple也是不可更改的
tt = ('aa', 'bb', ('cc', 'dd'))
print("tuple:", tt)

# 如果元组里面只有一个元素，一般要加一个“，”进行处理
tOne = (22,)
print(tOne)

# 创建一个空元组
tnull = ()
print(tnull)

# list的嵌套
list_aa = [[1,3,3],"test",(3,3,3)]
# 获取第一个list的第二个数
print(list_aa[0][1])        

# 测试赋值
a,b = (2,3)
# a的值为2
print(a)  
# b的值为3          
print(b)
