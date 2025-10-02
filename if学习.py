# if-else用法
alien_color = 'red'
if 'green' in alien_color:
    print('yes,u got 5 scores')
else:
    print('u got 10 scores')
    
# if-elif用法
if 'green' in alien_color:
    print('5 score')
elif 'yellow' in alien_color:
    print('10 scores')
elif 'red' in alien_color:
    print('10 scores')

# 综合用法    
age = 1
if age < 2 :
    print('u are a baby')
elif age < 12 :
    print('u are kid')
elif age < 18 :
    print('u are a teenager')
else:
    print('u are adult')
    
# 练习


x = 0
if x:
    print("A")
else:
    print("B")
# if-elif-else语句中,if和elif如果为true则返回,如果为false直到执行某个elif到true,否则则是false则执行else
# 也就是说在if - elif1 -elif2 -elif3 - elif4 - else
# 如果if错-elif1错-elif2对则后面不执行
# 如果if错-elif都错,则执行else


a = False
b = True
if a and b:            
    print("1")
elif a or b:
    print("2")
else:
    print("3")
# 输出 1 还是 2 还是 3?
# a and b 是false,
# a or b  是true 所以直接执行elif
# 可以把if和elif都看作一个整体 这一个整体为false则执行 else




