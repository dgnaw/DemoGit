# 1. Nhập một xâu ký tự s. In ra xâu đảo của xâu vừa nhập
from collections import Counter


def nhap_xau(s):
    return list(s[::-1])
# 2. Hiển thị tất cả các xâu con của một xâu ký tự.
def ht_tatca_xaucon(s):
    xau_con = []
    for i in range(len(s)):
        for j in range (i+1,len(s)+1):
            xau_con.append(s[i:j])
    return xau_con
# 3. Đưa ký tự xuất hiện nhiều nhất trong xâu ký tự
def kytu_max(s):
    counter = Counter(s)
    return max(counter,key=counter.get)
# 4. Xóa các ký tự trùng nhau khỏi xâu.
def xoa_trung(s):
    return ''.join(dict.fromkeys(s))
# 5. Cho biết số nguyên âm, phụ âm và khoảng trắng trong xâu.
def songuyenam_phuam_khoangtrang(s):
    nguyenam = set("ueoaiUEOAI")
    nguyenam_dem = sum(1 for char in s if char in nguyenam)
    phuam_dem = sum(1 for char in s if char.isalpha() and char not in nguyenam)
    khoangtrang = s.count(' ')
    return nguyenam_dem, phuam_dem, khoangtrang
# 6. Cho biết xâu có biểu diễn một số nguyên dương không?
def xau_soduong(s):
    return s.isdigit() and int(s) > 0
# 7. Nhập ký tự X, xóa ký tự X khỏi xâu.
def xoa_kytux(s,x):
    return s.replace(x,' ')