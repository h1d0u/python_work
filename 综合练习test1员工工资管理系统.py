# 项目1：员工工资管理系统
# 需求描述：
# 公司需要开发一个员工工资管理系统，要求能够：
# 数据准备



# 任务要求：
# 1计算每个员工的平均工资
# 2找出工资最高的员工
# 3统计每个部门的平均工资



employees = [
    {"id": "001", "name": "张三", "department": "技术部"},
    {"id": "002", "name": "李四", "department": "销售部"},
    {"id": "003", "name": "王五", "department": "技术部"},
    {"id": "004", "name": "赵六", "department": "人事部"}
]

salary_records = {
    "001": [8000, 8200, 8500, 8300],  # 1-4月工资
    "002": [6000, 6500, 7000, 6800],
    "003": [7500, 7600, 7800, 7700],
    "004": [5000, 5200, 5300, 5400]
}



names = []
department = []

for item in employees:
    names.append(item['name'])
    department.append(item['department'])

for ids , salarys in salary_records.items():
    average_salary = sum(salarys)/len(salarys)
    print(f"{ids}:{average_salary}")


    



















