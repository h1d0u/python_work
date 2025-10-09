# 类基础

# 类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
# 类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
# 对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
# 实例化：创建一个类的实例，类的具体对象。


# 创建类

class Dog:                              # 这里创建了一个叫Dog的类                  类命名规范 首字母大写
                                        # 类里面的函数叫做方法现在介绍_init_方法
    def __init__(self,name,age):        # _init_定义的前缀一定会有self self.xxx
                                        # 这个self是一只狗自己 名字,年龄是狗的属性
        self.name = name                # 给狗设置名字
        self.age =  age                 # 给狗设置年龄
    
    def sit(self):                      # 这个sit和下面的roll叫做方法
        """模拟狗坐下"""
        print(f"{self.name}坐下了")
    
    def roll(self):
        '''模拟狗打滚'''
        print(f"{self.name}在打滚")

dog1 = Dog("wei",6)                     # 这是一个六岁的叫wei的狗
dog2 = Dog("js",91)                     # 两只狗的self是不同的


dog1.sit()                              # 使用self.xxx()调用方法
dog2.sit()                  



# 下面练习

class Car:
    def __init__(self,make,model,year):
        """初始化car属性"""
        self.make = make
        self.model = model
        self.year = year
        self.mile = 2345                   # 可以给属性指定默认值
    
    def information(self):
        ifm = f"{self.make},{self.model},{self.year}"
        return ifm
    
    def read(self):
        '''打印里程数'''
        print(f"里程数为{self.mile}")
        
    
    def change(self,change_mile):
        """修改属性值
           禁止回调属性值
        """
        
        if change_mile >= self.mile:
            self.mile = change_mile
        else:
            print("wrong")


car1 = Car("lexus","rx","2023")

car1.change(231)

car1.read()


