import requests


response = requests.get('https://jsonplaceholder.typicode.com/posts')

 # Kiểm tra xem yêu cầu có thành công không (status code 200)
if response.status_code == 200:
        # Chuyển đổi dữ liệu JSON thành đối tượng Python
        sach_data = response.json()

        # In tổng số bài post
        print(f"Tổng số bài post: {len(sach_data)}\n")

        # In thông tin từng bài post
        for sach in sach_data:
            print("User:",sach['userId'])
            print("ID bài đăng:",sach['id'])
            print("Tiêu đề:",sach['title'])
            print("Nội dung:", sach['body'])
            print("==================================")
else:
        print(f"Yêu cầu không thành công. Mã trạng thái: {response.status_code}")

