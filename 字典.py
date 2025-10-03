information = {
    'firstname': 'chiaki',
    'lastname' : 'nanami',
    'age' : '21',
    'city' : 'tokyo'
    }
print(information)
print(len(information))

# 访问字典 information[]
print('firstname:' ,information['firstname'])
print('lastname:',information['lastname'])
print('age:',information['age'])
print('city:',information['city'])
    
# 创建空字典
emptyDict = dict()
print(emptyDict)

# 修改字典(向字典里添加了hobby job)
emptyDict['hobby'] = 'gaming'
emptyDict['job'] = 'student'
print(emptyDict)

# 删除字典
emptyDict['loving'] = ['cat']
print(emptyDict)

del emptyDict['loving']
print(emptyDict)



# 遍历字典
# for k,v in xxx.items()
for key,value in information.items():
    print(key)
    print(value)

