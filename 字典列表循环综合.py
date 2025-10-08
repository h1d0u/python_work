# 字典列表循环综合

# 1 列表间移动元素
# 网站用户分为认证用户，未认证用户 ,认证后将未认证用户移到已认证用户列表里面

unconfirmed_users = ["hedou","awei","ma","zhu"]
confirmed_users = []

while unconfirmed_users:                                      # 这行代码的意思是：当列表不为空时，循环继续；列表为空时，循环结束
    temp_users = unconfirmed_users.pop()                      # 在这里pop的对象会放在储存的最底层
    print(f"正在验证用户：{temp_users}")
    
    confirmed_users.append(temp_users)                        # 所以最先append的是zhu,此时confirmed_users 的列表会是反过来的 可以使用pop(0)调换顺序

print("\n 下列用户已认证：") 
for confirmed_user in confirmed_users:
    print(confirmed_user.title())                             # 这里为什么要用单数呢?


# 2 删除列表的特定元素
loving = ["nanami","cute","beauty","money","sporting","sporting","sporting"] #出现了多个sporting

while "sporting" in loving:
    loving.remove("sporting")                                 # 如果想要保留一个sporting怎么办呢 
                                                              # while "sporting" in loving and loving.count("sporting") > 1: 但是程式效率可能比较低
print(loving)                                                 # 不要想着用if语句 会有无限循环的风险



# 3 将输入的信息储存的字典里面
# 字典为 {name:hobby}
responses = {}

agree = True            #用户同意则为true 不同意则为false

while agree:
    #获取姓名和爱好
    name = input("what's your name")
    hobby = input("what's your hobby")
    
    #储存姓名和爱好
    responses[name] = hobby
    
    #别人是否想要继续
    repeat = input("你愿意继续参加吗y/n")
    if repeat == "n":
        agree = False
    elif repeat == "y":
        continue
    else:
        print("wrong input, please enter 'y' or 'n'")
        
       
        
print("==========results===========")

for name,hobby in responses.items():        
     print(f"{name}的爱好是{hobby}")



# Tips:字典中相同键的值会被覆盖  连续输入"Alice", reading";"Alice", swimming;"Alice",  "cooking"最后只会输出 Alice",  "cooking"