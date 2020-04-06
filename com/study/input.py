'''
    输入与格式化输出
'''
import sys

name = input("Name:")
age = input("Age:")
salary = input("Salary:")

path = sys.path

mes = '''----index of %s--------
Name: %s123
Age : %s
Salary: %s
''' % (name, name, age, salary)

print(mes)

print(path)


