# 自定义一个类
class MyClass:
    i = 123
    # 定义一个私有变量,私有属性在类外部无法直接进行访问，可以通过一个方法进行访问获取值
    __n = 0
    # 构造方法
    def __init__(self):
        print("构造方法,实例化类的时候就会被调用")

    # 重载构造方法
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    # 给私有变量赋值
    def setInit(self):
        # 访问私有变量
       return self.__n

    def f(self):
        return "Hello World"

# 类的实例化
x = MyClass("hello","你好","11")

# 访问类的变量
print("类变量 %d" % x.i)
# 访问类的方法
print("调用了类的方法 %s，" % x.f.__name__, "并且打印了类的方法的数据",x.f())
# 打印重载的变量数据
print(x.a,x.b,x.c,x.setInit())

