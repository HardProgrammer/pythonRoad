'''
    函数的作用域
    LEGB规则，表示的是Local -> Enclosed -> Global -> Built-in，其中的箭头方向表示的是搜索顺序。
        Local 可能是在一个函数或者类方法内部。
        Enclosed 可能是嵌套函数内，比如说 一个函数包裹在另一个函数内部。
        Global 代表的是执行脚本自身的最高层次。
        Built-in 是Python为自身保留的特殊名称。
'''

a = 10


def globel_func():
    a = 11  # Enclosed
    # 这边不是改变全局变量a的值，而是输出当前函数的变量值，相当于这边的a是另一个变量
    print(a)

    def inner_func():
        b = 20  # local 局部变量
        print("a = ", a, "b = ", b)

    # 函数的嵌套，只能在内部进行调用
    inner_func()


globel_func()
