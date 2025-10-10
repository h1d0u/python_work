# 类练习

# 创建一个User类 包含firstname,finalname,age,gender
# 定义一个describe_user的方法 打印信息
# 定义一个greet_user的方法 问候用户
# 给user类 添加一个login_attempts属性
# 增加一个change_attemps方法用于用户的增减
# 增加reset_login_attemps方法用于重置login_attemps
# 创建Admin类 继承user
# Admin添加privileges属性 privileges储存了admin的权限 创建show_privilege方法创建一个Admin实例调用这个方法
# 编写Privileges类 属性privilege 储存权限 在Admin类中 将Privileges实例用作其属性 创建Admin实例 调用show_priilege方法



class User:
    def __init__(self,firstname,finalname,age,gender,user_id,login_attempts=0):
        """创建了firstname finalname age gender"""
        self.firstname = firstname
        self.finalname = finalname
        self.age = age
        self.gender = gender
        self.user_id = user_id
        self.login_attempts = login_attempts
        
    def describe_user(self):
        """打印用户信息"""
        print(f"用户的名字叫做{self.firstname} {self.finalname},年龄是{self.age},性别是{self.gender}")
              
    def greet_user(self):
        """问候用户"""
        print(f"你好{self.firstname}")
    
        
    def change_attempts(self,nums):
        """用于用户的增减"""
       
        self.login_attempts += nums
        print(f"登录次数已更新为：{self.login_attempts}")

 
    def reset_login_attempts(self):
        """用于重置用户登陆"""
        self.login_attempts = 0
        print("登录次数已重置")
        
        
        
        
        
class Privileges:
    def __init__(self, privileges=None):
        """初始化管理员权限"""
        if privileges is None:
            privileges = ["添加用户", "删除用户", "封禁账号"]
        self.privileges = privileges

    def show_privileges(self):
        """显示管理员权限"""
        print("管理员拥有以下权限：")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    def __init__(self, firstname, finalname, age, gender, user_id, login_attempts=0):
        """初始化父类属性"""
        super().__init__(firstname, finalname, age, gender, user_id, login_attempts)
        
        """初始化子类独有属性"""
        self.privileges = Privileges()                    # 创建Privileges实例
    
    
    def show_privilege(self):
        """调用 Privileges 的显示方法"""
        self.privileges.show_privileges()                 #=====想一想这一步=====#
        


 # 使用示例
if __name__ == "__main__":
    # 创建实例
    admin = Admin("李", "管理员", 30, "男", "admin001")
    user = User("李", "管理员", 30, "男", "admin001")
    # 测试User类的方法
    admin.describe_user()
    admin.greet_user()
    
    # 测试Admin类的方法
    admin.show_privilege()

    # 测试权限管理
    print("\n直接通过privileges属性调用：")
    admin.privileges.show_privileges()       
        
