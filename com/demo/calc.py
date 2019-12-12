'''
实现简单的计算器：
    通过定义不同的函数来实现不同的运算    
'''

def add(x, y):
    # 两数相加
    return x + y


def sustract(x, y):
    # 两数相减
    return x - y


def multiply(x, y):
    # 两数想乘
    return x * y


def divide(x, y):
    # 两数相除，这里要禁止y为0
    if y == 0:
        print("除数不能为0")
        return 0
    return x / y


# 用户输入
print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")

choice = input("请输入你的选择（1/2/3/4）")

num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))

# 测试
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))
elif choice == '2':
    print(num1, "-", num2, "=", sustract(num1, num2))
elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("非法输入")
