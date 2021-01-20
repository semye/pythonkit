# 标准数据类型

# 注释
# 使用#号注释
# 多行注释使用'''和"""

# Number(数字)
# String(字符串)
# List(列表)
# Tuple(元组)
# Set(集合)
# Dictionary(字典)

# 不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）
# 可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）

# Number
# python中数字有四种类型：整数、布尔型、浮点数和复数。
# 整数
a = 1
# 布尔型
b = True
# 浮点数
c = 1.23
# 复数
d = 1 + 2j

print(a)
a = 2
print(a)

# 判断是否是指定的类型 isinstance
print(isinstance(a, int))
print(isinstance(b, bool))
print(isinstance(c, float))
print(isinstance(d, complex))

# type()不会认为子类是一种父类类型
# isinstance()会认为子类是一种父类类型

# 数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
# 在混合计算时，Python会把整型转换成为浮点数

# String

# # 字符串
# # 单引号和双引号使用完全相同
# # 使用三引号可以指定一个多行字符串
#
#
word = '字符串'
wuhan = "武汉"
shanghai = '''上海'''


# List(列表)
# 有序
# 使用[]列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）

lpl = ['rng', 'ig', 'edg', [1, 2, 3]]

# Tuple(元组)
# 与列表类似 元组的元素不能修改
tuple1 = ('abcd', 786, 2.23, 'wuhan', 70.2)

# Set(集合)
# 集合中的元素类型必须一致
# 通常会用{}来创建集合 只有创建空集合时才使用set()
# 创建一个空集合
set1 = set()
# 创建非空集合
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
pop1 = student.pop()
print("=====>" + pop1)
# set可以进行集合运算
seta = set('abracadabra')
setb = set('alacazam')
print(seta - setb)  # a和b的差集
print(seta | setb)  # a和b的并集
print(seta & setb)  # a和b的交集
print(seta ^ setb)  # a和b中不同时存在的元素

# dictionary(字典)
# 通过键来存取
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
# 定义空字典
dict = {}
