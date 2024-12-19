# 1. Nhập thông tin người dùng tên và số điện thoại vào danh bạ cho tới khi không muốn
# nhập nữa.

def nhap_thongtin(phonebook):
    while True:
        name = input("Nhap ten nguoi dung ('nhan enter' de stop):")
        if not name:
            break
        so_dien_thoai = input("Nhap so dien thoai:")
        phonebook[name] = so_dien_thoai
    return phonebook
# 2. Xóa thông tin của người có tên “Hoa”
def xoa_ten_Hoa(phonebook):
    if "Hoa" in phonebook:
        del phonebook["Hoa"]
        print("Da xoa thong tin nguoi ten 'Hoa'")
    else:
        print("Khong tim thay Hoa trong danh ba")
# 3. Tìm tên người dùng có số điện thoại nhập từ bàn phím
def tim_nguoi_sdt(phonebook):
   phone  = input("Nhap so dien thoai de tim nguoi:")
   for name,so_dien_thoai in phonebook.items():
       if so_dien_thoai == phone:
           print(f"Ten:{name}")
           return
   print("Khong tim thay so trong danh ba!")
# 4. Chèn thông tin một người vào danh bạ
def chen_thongtin(phonebook):
    name = input("Nhap ten can chen:")
    so_dien_thoai = input("Nhap sdt de chen:")
    phonebook[name] = so_dien_thoai
    print(f"Da chen {name} vao danh ba")