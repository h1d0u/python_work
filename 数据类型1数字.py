# 数据类型1 数字

# 数字:
#     int:整数,
#     float:浮点数 
#     complex:复数
# 数字类型转换:
#            int(x)
#            float(x)
# 数字运算:
#         +
#         -'
#         *
#         /
#         //   除法取整
#         %    除法去余数
#         **n  n次方


# 斐波那契数列
a,b = 0 ,1
while a < 100000:
    a,b = b, a+b
    print (a)