# 函数知识点补充


# Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。
# 模块是一组Python代码的集合，可以使用其他模块，也可以被其他模块使用。

# 创建模块时，要注意：
# 模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
# 模块名不要和系统模块名冲突

# 当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。

   
# 导入整个模块
# import modtest
# 导入所有模块的所有函数
# from modtest import *  但这个方法不好 容易发生冲突

import math              #注意 原模块里面需要import math 这里才能import math

# 引入特定函数
from modtest import move as mv, solve_quadratic as sq
# as既可以给模块别名 也可以给函数别名

mv(3, 'A', 'B', 'C')

result_0 =sq(1,-2,1)
print(result_0) 



# 使用dir()查找模块定义的名称