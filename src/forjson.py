# json 模块用法
import json

file = open("../resources/1.json", "r")
# json.loads 操作字符串
# json.load 操作字符流
data = json.load(file)
file.close()
print("打印字典")
print(type(data))
print(data)
# 字典转json string
json_str = json.dumps(data)
print(type(json_str))
print(json_str)
