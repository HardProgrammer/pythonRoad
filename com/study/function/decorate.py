# 装饰器： 极大简化代码，避免每个函数编写重复性代码
from functools import reduce

def new_fn(f):
    # *args 和 **kw，保证任意个数的参数总是能正常调用
    def fn(*args,**kw):
        r = f(*args,**kw)
        print("开始进行...")
        return r
    return fn

@new_fn
def f1(n):
    print("执行f1...")
    return reduce(lambda x,y:x*y,range(1,n+1))

print(f1(3))