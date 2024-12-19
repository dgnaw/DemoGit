# 1. Nhập thông tin tên sách và số lượng sách tương ứng vào một dictionarie cho tới khi
# không muốn nhập nữa.
def nhap_tt():
    mybook = {}
    while True:
        name = input("Nhap ten sach (hoac go 'stop' de dung):")
        if name.lower() == "stop":
            break
        sl_book = int(input("Nhap so luong sach:"))
        mybook[name] = sl_book
    return mybook
# 2. Tổng số sách là bao nhiêu?
def tong_sach(mybook):
   return sum(mybook.values())
# 3. Những sách nào có số lượng 10 quyển
def sach_10quyen(mybook):
    ket_qua = []
    for name,sl_book in mybook.items():
        if sl_book == 10:
            ket_qua.append(name)
    return ket_qua

# 4. Xóa đi những sách có số lượng dưới 5 quyển.
def xoa_sach_duoi5quyen(mybook):
    ketqua = {}
    for name,sl_book in mybook.items():
        if sl_book >= 5:
            ketqua[name] = sl_book
    return ketqua