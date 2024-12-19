# 1. Nhập thông tin người dùng tên và mật khẩu vào một dictionarie cho tới khi không
# muốn nhập nữa.
def nhap_thongtin(myaccount):
    while True:
        name = input("Nhap ten nguoi dung (nhan 'enter' de dung):")
        if not name:
            break
        password = input("Nhap mat khau :")
        myaccount[name] = password
    return myaccount
# 2. Kiểm tra xem có mật khẩu nào không hợp lệ (mật khẩu hợp lệ là xâu ký có 7 ký tự, ký
# tự bắt đầu là chữ hoa)
def kt_mk_khong_hople(myaccount):
    khong_hop_le = []
    for name,password in myaccount.items():
        if len(password) != 7 or not password[0].isupper():
            khong_hop_le.append(name)
    return khong_hop_le
# 3. Tìm mật khẩu người dùng có tên nhập từ bàn phím
def tim_mk_users(myaccount):
    nhap_ten = input("Nhap ten nguoi can tim:")
    for name,password in myaccount.items():
         if name == nhap_ten:
             print(f"Nguoi dung ten {name} co password la :{password}")
             return
    print("Khong tim thay nguoi dung !")
# 4. Mật khẩu người dùng nào tất cả là chữ hoa
def mk_chuhoa(myaccount):
    chu_hoa = []
    for name,password in myaccount.items():
        if password.isupper():
            chu_hoa.append(name)
    return chu_hoa