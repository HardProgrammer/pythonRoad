# 装饰器： 极大简化代码，避免每个函数编写重复性代码
import functools

# 表示传输的参数不固定
def new_fn(f):
    # *args 和 **kw，保证任意个数的参数总是能正常调用
    def fn(*args,**kw):
        r = f(*args,**kw)
        print("开始进行...")
        return r
    return fn

@new_fn
def f1(n):
    print("执行%s..." % f1.__name__)
    return n + n

print(f1(3))


@new_fn
def f2(n):
    print("执行%s..." % f2.__name__)
    return n * n

print(f2(3))

#增加@functools.wraps(f), 可以保持当前装饰器去装饰的函数的 __name__ 的值不变
def user_login_data(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

@user_login_data
def login1():
    print("开始执行login1... %s" % login1.__name__)

if __name__ == '__main__':
    # 获取的是wrapper
    print(login1.__name__)
    print(login1())