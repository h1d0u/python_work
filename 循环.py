# for循环
# for循环可以遍历任何序列的项目，如一个列表或者一个字符串。


for letter in 'Python':     
   print(f"当前字母是{letter}")
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:       
   print (f'当前水果是{fruit}')
 
print ("Good bye!")



# while循环
# while 语句用于循环执行程序,直到条件不再满足为止

num_0 = 0
while num_0 <= 3:
    print(num_0)                         
    num_0 += 1                                      #此处+= 和 num_0 = num_0 + 1 相同

num_1 = 0
while True:
    user_input =input('按c继续,按q退出')              #可以使用.strip().lower()针对大小写和可空格
    if user_input == "q":                   
       print('end')
       break                                        #此处break终止的是当前最外层的循环也就是while
    if user_input == "c":
       print(num_1)
       num_1 += 1
    else:
      print("wrong press")


# break的用法                                         break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句

# # 外层循环
# while condition1:
#     # 内层循环  
#     while condition2:
#         # 更内层循环
#         for i in range(10):
#             break  # 终止的是最内层的for循环          #break只会终止它所在的当前循环层级



# continue
# continue 语句跳出本次循环，而break跳出整个循环

# 输出0-10 跳过偶数
num_2 = 0
while num_2 < 10:
   num_2 += 1
   if num_2 % 2 == 0:
      continue
   print(num_2)