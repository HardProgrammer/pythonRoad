# 类的实例测试
class Car:
    def __init__(self, color, name , **kwargs):
        self.color = color
        self.name = name
        for k,w in kwargs.items():
            # 添加更多的参数
            setattr(self,k,w)


car = Car("red","lll",size="big")

print(car.size)