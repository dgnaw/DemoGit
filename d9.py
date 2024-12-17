# 1. Nhập thông tin người dùng và số điện thoại vào danh bạ cho tới khi không muốn nhập nữa.
def nhap_thongtin(myphone):
    while True:
        name = input("Nhap ho ten nguoi dung (go 'enter' de dung): ").strip()
        if name.lower() == "enter":
            break
        numbers_phone = input("Nhap so dien thoai vao danh ba:").strip()
        myphone[name] = numbers_phone
# 2. Hiển thị toàn bộ danh bạ được sắp xếp từ Z đến A theo họ tên.
def ht_danhba_sx_theoten(myphone):
    print("Danh ba sap xep tu Z den A:")
    for name in sorted(myphone.keys(),reverse = True):
        print(f"{name}:{myphone[name]}")
# 3. Nhập một xâu ký tự từ bàn phím, tìm và hiển thị tất cả những người có họ tên chứa xâu kí tự
# vừa nhập cùng số điện thoại tương ứng
def tim_hienthi(myphone,keyword):
    print(f"Ket qua tim kiem voi '{keyword}':")
    found = 0
    for name,numbers_phone in myphone.items():
        if keyword.lower() in name.lower():
            print(f"{name}:{numbers_phone}")
            found = 1
    if not found:
        print("Khong tim thay lien lac !")
# 4. Nhập vào một chuỗi số, hiển thị tên của người có số điện thoại vừa nhập
def ht_tennguoi_sdt(myphone,phone_number):
    for name,numbers_phone in myphone.items():
        if numbers_phone == phone_number:
            print(f"So dien thoai '{phone_number} thuoc ve {name}")
            return
    print(f"Khong tim thay lien lac voi so dien thoai: '{phone_number}'")