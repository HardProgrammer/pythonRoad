'''
    获取输入框的内容:
        python2中使用的是raw_input()获取输入内容，python3没有
'''

# 输入信息
name = input("your name:")
age = input("your age:")

# 获取变量的数据类型，在输入语句中，默认获取的数据为字符串（str）类型
print (type(age))

print("name = ",name ,",age = ", age)

# 强制类型转换--字符串换整型
age_int = int(age)

print("age_int = ", age_int)
