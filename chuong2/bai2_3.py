import xml.dom.minidom

# Đường dẫn tương đối đến tệp XML
file_path = "C:\Thuc_hanh\Chuong_2\sample.xml"  
def main():

    # Tải tệp XML
    doc= xml.dom.minidom.parse(file_path)

    # Lấy root element
    company = doc.documentElement
    print(f"Root element: {company.tagName}")

    # Lấy thông tin về công ty
    company_name = company.getElementsByTagName("name")[0]
    print(f"Company name: {company_name.firstChild.data}")
    print(company_name.getAttribute("name"))
    # Lấy thông tin về nhân viên
    staff_list = company.getElementsByTagName("staff")
    for staff in staff_list:
        staff_id = staff.getAttribute("id")
        name = staff.getElementsByTagName("name")[0]
        salary = staff.getElementsByTagName("salary")[0]
        print(f"\nStaff ID: {staff_id}")
        print(f"Name: {name.firstChild.data}")
        print(f"Salary: {salary.firstChild.data}")
if __name__ == "__main__":
    main()


