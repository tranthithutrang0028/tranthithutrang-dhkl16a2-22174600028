import json
# Đối tượng Python (đối tượng JSON)
data = {
    "name": "Lan",
    "age": 19,
    "city": "Hà Nội"
}
# Chuyển đối tượng Python thành chuỗi JSON
json_string = json.dumps(data, ensure_ascii=False)
print(json_string)
