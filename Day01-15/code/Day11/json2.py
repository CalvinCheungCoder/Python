import json

teacher_dict = {'name': 'Calvin', 'age': 25, 'title': '讲师'}
json_str = json.dumps(teacher_dict)
print(json_str)
print(type(json_str))
fruits_list = ['apple', 'orange', 'strawberry', 'banana', 'pitaya']
json_str = json.dumps(fruits_list)
print(json_str)
print(type(json_str))
