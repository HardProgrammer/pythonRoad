'''
    获取输入框的内容:
        python2中使用的是raw_input()获取输入内容，python3没有
'''
import getpass

# 输入信息
name = input("your name:")
age = input("your age:")
# 隐藏输入
password = getpass.getpass("your password:")

# 获取变量的数据类型，在输入语句中，默认获取的数据为字符串（str）类型
print (type(age))

print("name = ",name ,",age = ", age, ",password = ", password)

# 强制类型转换--字符串换整型
age_int = int(age)

print("age_int = ", age_int)
