# 1. Để quản lý thư viện, người dùng có thể nhập một chuỗi các từ là tên các sách cách
# nhau bởi dấu phẩy.
def ql_thuvien():
    tensach = input("Nhap chuoi cac tu la ten sach cach nhau boi dau phay:")
    return tensach.split(',')
# 2. Tách các từ trong chuỗi theo dấu phẩy, sắp xếp chúng theo thứ tự bảng chữ cái.
def tach_sx_bangchucai(ten_sach):
    return sorted(ten_sach)
# 3. Xóa các tên sách trùng nhau khỏi danh sách
def xoa_sach_trung(ten_sach):
    return list(set(ten_sach))
# 4. Tên sách nào dài nhất.
def max_sach(ten_sach):
    maxsach = max(ten_sach,key = len)
    return maxsach