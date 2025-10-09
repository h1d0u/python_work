import math

# 定义函数

# 空函数
def nop():
    pass                                                # pass将没想好的功能跳过,先让函数跑起来,以便后续改动


# 函数返回值                                          # 函数运行完毕后，返回给调用者的值
# 语法:

# def 函数(参数1,参数2...):
#     函数结构
#     return 返回值

def add(a,b):
    result = a + b
    return result       
print("done")                                       # 这个print不会运行 函数只要执行到return就不会再执行了

r = add(4,5)
# print(add)                                        # 不要犯这个错误 不要print函数本身
print(r)


# 无返回值返回 None
def test():
    return
#   return None                                     # 这两个都一样,函数都会返回None,可以用作False
#   return print("字符串")：在函数内部就完成了输出，相当于返回None，调用者无法获得有用信息





# 返回多个值               
def move(x,y,step,angle=0):
    """_summary_
move 给出原坐标,位移和角度 计算新坐标 (有bug step必须大于0)
    Args:
        x (_type_): 原坐标x
        y (_type_): 原坐标y
        step (_type_): 位移长度
        angle (int, optional): 位移角度.默认为0,使用弧度制

    Returns:
        : 返回新的坐标(xn,yn)
    """
    rad = math.radians(angle)                          # 将角度转化成弧度制   
    xn = x + step * math.cos(rad)
    yn = y - step * math.sin(rad)                      # 计算机屏幕顶部为0 向下为y+
    return xn , yn

r = move(3,4,6.67,math.pi/2)
print(r)


# 返回字典和列表
def information(firstname,secondname,age=None):
    """返回字典,包含人的信息"""
    person = {"first" : firstname,"last" : secondname}
    if age:
        person["age"] = age
    return person

i = information("h","d",age = 3)
print(i)