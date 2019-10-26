# 类的继承
class ParentClass:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("父类构造方法")

    def printMyclass(self):
        print("父类的基本方法2")

# 多继承，一子类可以继承多个父类
class parentClass1:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def printMyclass(self):
        print("父类的基本方法")
    
    def printThisClass(self):
        print("this class is ...")


class sonClassEx(ParentClass, parentClass1):
    def __init__(self):
        ParentClass.__init__(self)
        parentClass1.__init__(self)


    # 重写父类
    def printThisClass(self):
        print("hello World")

son = sonClassEx()
# 方法名同，默认调用的是在括号中排前地父类的方法
son.printMyclass()
# 重写后打印出的是子类的值
son.printThisClass()