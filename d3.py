# 1. Nhập một xâu ký tự. In ra tất cả các ký tự trong xâu vừa nhập
def hienthixaukt(s):
    print("Cac ky tu trong xau:",*s)
# 2. In xâu đảo ngược của xâu ký tự vừa nhập.
def daonguoc_kytu(s):
    print("Xau dao nguoc:",*s[::-1])
# 3. Nhập 1 xâu con s1, tìm số lần xuất hiện của s1 trong s.
def solanxuathiens1(s,s1):
    print(f"So lan xuat hien cua {s1} trong {s} la:",s.count(s1))
# 4. Nhập 1 xâu ký tự s2, kiểm tra xem xâu s có bắt đầu bằng s2 hay không?
def kiemtra_sbangs2(s,s2):
    print(f"Xau co bat dau bang {s2} khong ? : ",s.startswith(s2))
# 5. Đưa ra ký tự xuất hiện ít lần nhất trong xâu ký tự vừa nhập.
def kytuxuathien_itnhat1lan(s):
    min_char = min(s, key = s.count)
    print("Ky tu xuat hien it lan nhat la:",min_char)
# 6. Xâu vừa nhập có bắt đầu bằng chữ hoa không?
def kiemtra_batdauviethoa(s):
    print(f"Xau co bat dau bang chu hoa khong ? : ",s[0].isupper() if s else False)
# 7. Hiển thị tất cả các xâu con của xâu ký tự vừa nhập
def xaucon_danhap(s):
    print("Tat cac cac xau con:")
    for i in range ((len(s))):
        for j in range (i+1,len(s) + 1):
            print(s[i:j])
# 8. Đếm chữ hoa, chữ thường trong xâu vừa nhập
def demchuhoa_chuthuong(s):
    upper = sum (1 for c in s if c.isupper())
    lower = sum (1 for c in s if c.islower())
    print(f"So chu hoa:{upper}, So chu thuong:{lower}")
# 9. Sắp xếp các ký tự trong xâu vừa nhập theo thứ tự tăng dần
def sx_tangdan(s):
    print("Xau sau khi sap xep tang dan la:",''.join(sorted(s)))
# 10. Nhập một xâu con s1, kiểm tra xem xâu ký tự s có kết thúc bằng xâu s1 hay không?
def kiemtra_ketthuc(s,s1):
    print(f"Xau {s} co ket thuc bang xau {s1} :",s.endswith(s1))
# 11. Đưa ra ký tự xuất hiện nhiều lần nhất trong xâu ký tự vừa nhập.
def kytu_xuathiennhieulannhat(s):
    max_char = max(s, key = s.count)
    print(f"Ky tu {max_char} xuat hien nhieu lan nhat")
# 12. Kiểm tra xem các từ trong xâu ký tự s có bắt đầu bằng chữ hoa hay không(từ là các ký tự liền
# nhau không chứa dấu cách)?
def kiemtra_tuscoviethoa(s):
    words = s.split()
    print("Cac tu bat dau bang chu hoa khong ? :",all(word[0].isupper() for word in words if word))
# 13. Tách xâu ký tự thành các từ riêng biệt và in ra các từ đó trên các dòng khác nhau (từ là các ký
# tự liền nhau không chứa dấu cách)?
def tach_xau_roiin(s):
    words = s.split()
    print("Cac tu trong xau:")
    for word in words:
        print(word)
# 14. Xóa từ cuối cùng khỏi xâu
def xoa_tucuoi(s):
    words = s.split()
    print("Xau sau khi xoa tu cuoi:",''.join(words[:-1]))
# 15. Tìm số lượng từ trong một xâu ký tự (từ là các ký tự liền nhau không chứa dấu cách)?
def soluongtu(s):
    words = s.split()
    print("So luong tu xuat hien trong xua ky tu la:",len(words))
# 16. Đưa ra ký tự xuất hiện ít lần nhất trong xâu ký tự vừa nhập.
# 17. Nhập xâu s1, kiểm tra xem xâu s1 có phải là đảo ngược của xâu s không?
def kiemtra_daonguoc(s,s1):
    print(f"{s1} co phai dao nguoc cua {s} khong ? ",s1 == s[::-1])
# 18. kiểm tra xem một chuỗi có phải là chuỗi đối xứng không?
def kiemtra_chuoidx(s):
    print("Xau co phai chuoi doi xung?",s == s[::-1])
# 19. Đếm số từ trong một chuỗi (từ là các ký tự liền nhau không chứa dấu cách)
# 20. Xóa tất cả các chữ số trong xâu
def xoa_tatcachuso(s):
    print("Xau sau khi xoa :",''.join(c for c in s if not c.isdigit()))
# 21. Tìm từ ngắn nhất trong chuỗi (từ là các ký tự liền nhau không chứa dấu cách)
def timtunganhat(s):
    words = s.split()
    shortest = min(words,key = len)
    print("Tu ngan nhat trong xau la: ",shortest)
# 22. Đếm tổng số ký tự chữ cái trong một chuỗi.
def dem_kytuchucai(s):
    letters = sum(1 for c in s if c.isalpha())
    print("Tong so ky tu chu cai:",letters)
# 23. Kiểm tra xem một chuỗi có phải toàn bộ là chữ hoa không
def kiemtra_chuoiviethoa(s):
    print("Chuoi toan bo chu hoa ?",s.isupper())