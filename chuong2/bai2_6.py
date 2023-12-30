import json

# Đối tượng Python (dictionary)
python_obj = {"name": "Lan", "age": 19, "city": "Hà Nội"}
# Chuỗi JSON bao quanh bằng dấu nháy kép
python_obj2= "{\"Tên\": \"Lan\", \"Tuổi\": 19, \"Thành Phố\": \"Hà Nội\"}"
# Chuyển chuỗi JSON thành đối tượng Python (đối tượng JSON)
json_object_1 = json.loads(python_obj2)
print(json_object_1)

