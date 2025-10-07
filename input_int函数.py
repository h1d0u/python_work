# input()函数  int()函数

# 函数语法: input([prompt])     int(number)
# input() 用于接受一个标准输入数据，返回为 字符串 类型
# int()   用于将一个字符串或数字转换为     整数


msg = input("what's your name:")
print(f"your name is : {msg}")


age = input("how old are u?")                  # 此时age会返回字符串类型
age = int(age)                                 # 如果不使用int函数下面的判断会报错
if 18 > age > 12:
    print("teenager")
else:
    print("not teenager")

# 奇偶判断器
num = int(input("输入一个数字:"))
if num % 2 == 0:
    print("it's even")
else:
    print("it's odd")

