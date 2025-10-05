# 字典格式: d = {key1: value1, key2: value2, key3: value3}
# 其中 key 为键; value 为值 

information = {
    'firstname': 'chiaki',
    'lastname': 'nanami',
    'age': '21',
    'city': 'tokyo'
}

print("完整字典:", information)
print("字典长度:", len(information))



# 字典的特性
# 1  值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的
# 2  键必须不可变，所以可以用数字，字符串或元组充当，不可以使用列表
# 3  不允许同一个键出现两次。创建时如果同一个键被赋值两次，前一个值会被后一个值覆盖


tinydict = {'Name': 'gk', 'Age': 20, 'Name': 'hedou'}
print ("tinydict['Name']: ", tinydict['Name'])                   #此时会输出  tinydict['Name']:  hedou  ;而不是  tinydict['Name']:  gk





# 字典的操作与访问
# 1   访问字典中的值
print('\n--- 访问字典值 ---')
print('firstname:', information['firstname'])                    #类似于字典xxx[key_n] 即可访问value_n
print('lastname:', information['lastname'])
print('age:', information['age'])
print('city:', information['city'])

# 2   创建空字典的两种方式
print('\n--- 空字典操作 ---')
emptyDict = dict()                                               # 或者 emptyDict = {}
print("空字典:", emptyDict)

# 3   添加键值对
emptyDict['hobby'] = 'gaming'
emptyDict['job'] = 'student'
print("添加后:", emptyDict)

# 4   删除字典的键值对
emptyDict['loving'] = ['cat']
print("添加loving:", emptyDict)

del emptyDict['loving']                                         # 使用 del xxx[key_n] 进行删除
print("删除loving后:", emptyDict)

# 5   使用.get()方法安全访问值
print('\n--- get()方法演示 ---')
value_1 = information.get('gender', "there's no gender value")  #.get(key, default)
print("gender:", value_1)                                       #由于字典中没有gender键,因此value_1

value_2 = emptyDict.get('hobby', "")                            # 此时字典里有hobby，所以输出hobby的值
print("hobby:", value_2)

# 6   遍历字典的键值对
print('\n--- 遍历键值对 ---')                                     
for key, value in information.items():                          #for k,v in xxx.items():
    print(f"{key}: {value}")                                    #这个时候返回的是列表形式

# 7   遍历字典的键
print('\n--- 遍历键 ---')                                  
for key in information.keys():                                  #for k in xxx.keys():
    print(key)

# 8   遍历字典的值  
print('\n--- 遍历值 ---')
for value in information.values():                              #for v in xxx.values():
    print(value)

# 9   按特定顺序遍历字典的键
print('\n--- 按键排序遍历 ---')
for key in sorted(information.keys()):                          #for key in sorted (xxx.keys()):
    print(f"{key}: {information[key]}")
