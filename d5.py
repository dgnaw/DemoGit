# 1. Nhập một chuỗi số nguyên phân tách bằng dấu phẩy tạo ra một tuple chứa mọi số trong chuỗi
# số vừa nhập
def nhap_so(input_tuple):
    return tuple(map(int,input_tuple.split(',')))
# 2. Đưa tuple vừa nhập ra màn hình
def hienthi_tuple(t):
    print("Tuple:",t)
# 3. Đưa ra màn hình một nửa số giá trị đầu tiên trong 1 dòng và 1 nửa số giá trị cuối trong 1
# dòng.
def hienthi_nuadau_nuacuoi(t):
    n = len(t)
    first_half = n // 2
    end_half = n // 2
    return t[:first_half],t[end_half:]
# 4. Đưa ra màn hình các số chẵn có trong tuple vừa nhập trên 1 dòng và các số lẻ có trong tuple
# vừa nhập 1 dòng.
def so_chanvaso_le(t):
    chan = [x for x in t if x % 2 == 0]
    le = [x for x in t if x % 2 != 0]
    print("Chan:",chan)
    print("Le",le)
# 5. Nhập 1 số X, nếu X có trong tuple hãy xóa X khỏi tuple vừa nhập
def xoaX_danhap(t,x):
    return tuple(y for y in t if y!=x)
# 6. Đưa ra màn hình số lớn nhất có trong tuple vừa nhập
def solonnhat(t):
    return max(t)
# 7. Thay các số âm có trong tuple vừa nhập thành số 0.
def thayam_bang0(t):
    return tuple(0 if x < 0 else x for x in t)
# 8. Tách dãy số vừa nhập vào 2 tuple, 1 tuple chứa các số chẵn 1tuple chứa các số lẻ
def tach_tuple(t):
    chan = tuple(x for x in t if x % 2 == 0)
    le = tuple(x for x in t if x % 2 != 0)
    return chan,le