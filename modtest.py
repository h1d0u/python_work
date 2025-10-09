#  模块练习 此文件用于import演示

import math                                      #被导入的模块里如果使用了math 原模块也要使用

def solve_quadratic(a,b,c):
    delta = b**2 - 4*a*c                         # 算出判别式
    
    if delta < 0:                                
        return "无实数解"                         # 这里return print("无实数解") 会是什么样子呢
    elif delta == 0:
        x_0 = (-b + math.sqrt(delta))/(2*a)
        return x_0
    else:
        x_1 = (-b + math.sqrt(delta))/(2*a)
        x_2 = (-b - math.sqrt(delta))/(2*a)
        return x_1, x_2
    
    
# 汉诺塔
# 编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法


def move(n, o, p, q):
    if n == 1:
        print(f"{o} --> {q}")
    else:
        move(n - 1, o, q, p)
        print(f"{o} --> {q}")
        move(n - 1, p, o, q)