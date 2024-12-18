# 1. Nhập vào một dãy số nguyên cách nhau bằng dấu phẩy, chuyển đổi chúng thành một
# danh sách các số nguyên.
from math import factorial
def taolist(nhap_n):
    return list(map(int,nhap_n.split(',')))
# 2. Đưa ra số lớn nhất trong các số chia hết cho 3 có trong danh sách.
def max_chiahe3(ds):
    return max(x for x in ds if x % 3 == 0)
# 3. Đưa ra các số chính phương có trong danh sách
def scp(ds):
    import math
    scp = []
    for num in ds:
        can = math.sqrt(num)
        if can * can == num:
            scp.append(num)
    return scp
# 4. Nhập một số X từ bàn phím, X có trong danh sách không, nếu có chỉ ra vị trí cuối
# cùng của X trong danh sách
def vitricuoicung(ds,x):
    return len(ds) - 1 - ds[::-1].index(x) if x in ds else None
# 5. Đưa ra số nhỏ nhất trong các số dương có trong danh sách.
def min_soduong(ds):
    return min(x for x in ds if x > 0 )
# 6. Đưa ra giai thừa của các số có trong danh sách
def giaithua(ds):
    return [factorial(num) for num in ds]
# factorial(): dùng để tính giai thừa
# 7. Nhập một số X từ bàn phím, X có trong danh sách không, nếu có xóa X khỏi danh sách.
def kt_x(ds,x):
    # if x in ds:
    #     ds.remove(x)
    # return ds
    return [num for num in ds if num!= x]

# 8. Đưa ra trung bình cộng các số chia hết cho 3 có trong danh sách.
def tbc_chiahetcho3(ds):
    chiahet3 = [x for x in ds if x % 3 == 0]
    return sum(chiahet3) / len(chiahet3)
# 9. Số nào trong danh sách xuất hiện nhiều nhất
def so_xhmax(ds):
    if not ds:
        return []
    max_count = max(ds.count(x) for x in ds)
    return list(set(x for x in ds if ds.count(x) == max_count))
# 10. Xóa khỏi danh sách số ở vị trí thứ 3
def xoaso_vitri3(ds,position):
    if 0 <= position < len(ds):
        return ds[:position] + ds[position + 1:]
    return ds