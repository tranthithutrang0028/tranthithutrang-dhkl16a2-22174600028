import requests

# Địa chỉ API
api_url = "https://jsonplaceholder.typicode.com/comments"

# Post ID muốn hiển thị
post_id = 1

# Số lượng bài post muốn hiển thị
so_luong_hien_thi = 3

# Tạo địa chỉ API dựa trên post_id
api_url = f"{api_url}?postId={post_id}"

# Gửi yêu cầu GET đến API
response = requests.get(api_url)

# Kiểm tra xem yêu cầu có thành công không (status code 200)
if response.status_code == 200:
    # Chuyển đổi dữ liệu JSON thành đối tượng Python
    sach_data = response.json()
    # In danh sách các bài post nổi bật
    print(f"Danh sách các bài post nổi bật (Giới hạn 3 bài đầu):")

    for i in range(so_luong_hien_thi):
        sach = sach_data[i]
        print(f"{i+1}. {sach['name']}")

    print("\nDanh sách thông tin chi tiết của mỗi bài post:")
    # In thông tin từng bài post
    for i in range(so_luong_hien_thi):
        sach = sach_data[i]
        print(f"\nThông tin bài post {sach['id']}:")
        print(f"Name: {sach['name']}")
        print(f"Email: {sach['email']}")
        print(f"Body: {sach['body']}")
else:
    print(f"Không thể kết nối đến API. Status code: {response.status_code}")
