#1. Nhập vào một dãy số nguyên cho tới khi không muốn nhập nữa. In dãy vừa nhập ra màn hình
def nhapdayso():
    lst = []
    while True:
        try:
            n = int(input("Nhap so nguyen (hoac nhan Enter de dung):"))
            lst.append(n)
        except ValueError:
            break
    return lst
#2. Xóa toàn bộ các phần tử âm khỏi danh sách.
def xoa_ptuam(lst):
    return [x for x in lst if x>=0]
#3. Nhập 1 số X, đếm số lần xuất hiện X trong danh sách.
def count_x(lst,x):
    return lst.count(x)
#4. Nhập 1 số X, tìm các vị trí xuất hiện X trong danh sách.
def vitri_x(lst,x):
    return [i for i, val in enumerate(lst) if val == x]
#5. Đếm số phần tử khác nhau trong danh sách.
def count_phantukhac(lst):
    return len(set(lst))
#6. Xóa toàn bộ các phần tử trong danh sách.
def xoa_tatcaphantu(lst):
    return []
#7. Đưa ra trung bình cộng các só chia hết cho3 có trong danh sách vừa nhập.
def tbc_chia3(lst):
    chiahetcho3 = [x for x in lst if x%3==0]
    return sum(chiahetcho3) / len(chiahetcho3) if chiahetcho3 else 0
# 8. Xóa tất cả các số dương khỏi danh sách
def xoa_ptuduong(lst):
    return [x for x in lst if x < 0]
# 9. Đưa ra số chia hết cho 5 cuối cùng trong danh sách
def chiahet5_cuoicung(lst):
    for x in reversed(lst):
        if x % 5 == 0:
            return x
    return None
# 10.Đưa ra trung bình cộng các só âm có trong danh sách vừa nhập.
def tbc_soam(lst):
    so_am = [x for x in lst if x<0]
    return sum(so_am) / len (so_am) if so_am else 0
# 11. Thay thế tất cả các số âm trong danh sách thành số 0
def thaythe_soam_thanh0(lst):
    return [x if x >= 0 else 0 for x in lst]
# 12. Xóa các giá trị trùng lặp trong danh sách
def xoa_giatri_lap(lst):
    return list(dict.fromkeys(lst))
# 13. Tìm phần tử dương nhỏ nhất trong danh sách.
def phtu_minduong(lst):
    so_duong = [x for x in lst if x > 0]
    return min(so_duong) if so_duong else None
# 14. Đưa ra số lượng các số âm liên tiếp nhiều nhất.
def soluong_amlientiep(lst):
    max_count = count = 0
    for x in lst:
        if x < 0:
           count+=1
           max_count = max(max_count,count)
        else:
            count = 0
    return max_count
# 15. Đưa ra tổng và trung bình cộng các phần tử trong danh sách
def tongvatbc(lst):
    return sum(lst), sum(lst) / len(lst) if lst else (0,0)
# 16. Tìm các số hoàn hảo trong danh sách và in ra màn hình
def shh(n):
    if n < 2:
        return False
    return sum(i for i in range(1,n) if n%i ==0 ) == n
def ktra_shh(lst):
    return [x for x in lst if shh(x)]
