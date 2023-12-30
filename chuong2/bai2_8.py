import json

# Đối tượng từ điển Python được sắp xếp theo khóa
python_dict = {"name": "Lan", "age": 19, "city": "Hà Nội"}

# Chuyển đổi đối tượng từ điển thành chuỗi JSON với thụt lề 4
json_str = json.dumps(python_dict, indent=4)

# In ra các thành viên của đối tượng JSON
print(json_str)
