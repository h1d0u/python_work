# 类继承与多态



class Car:
    """三个属性 品牌 型号 年份 里程数
    """
    def __init__(self,make,model,year,mile=0):    
        """初始化car属性"""
        self.make = make
        self.model = model
        self.year = year
        self.mile = mile                   
    
    def information(self):
        ifm = f"{self.make},{self.model},{self.year}"
        return ifm
    
    def read(self):
        '''打印里程数'''
        print(f"{self.make}的里程数为{self.mile}")
        
    
    def change(self,change_mile):           
        """修改属性值
           禁止回调属性值
        """
        
        if change_mile >= self.mile:
            self.mile = change_mile
        else:
            print("wrong")
    
    def plus(self,mls):
        """增加了多少里程"""
        self.mile += mls                            # 不要写成self.plus

# 上面定义了一个名叫Car的大类 如果想要创建一个EvCar的小类 并且继承Car的属性
# 使用子类_init_方法

class EvCar(Car):
    
    def __init__(self, make, model, year):
        """初始化EvCar"""
        super().__init__(make, model, year)              # 这个super()函数使得EvCar可以调用Car的方法
        """给evcar增加了battary属性"""                     # 如果想要在子类添加新的属性直接添加即可 
        self.battary = 40    
    
    def read_battary(self):                              # 同理 直接添加方法即可
        print(f"电池容量为{self.battary}")

    
        


byd = EvCar("byd","u8",2222)
# 直接调用plus 和 read 方法
byd.plus(23)
byd.read()

byd.read_battary()




