'''
    输入与格式化输出
'''
name = input("Name:")
age = input("Age:")
salary = input("Salary:")

mes = '''----index of %s--------
Name: %s
Age : %s
Salary: %s
''' % (name, name, age, salary)

print(mes)


