# 1. Tạo 1 list gồm n phần tử chứa các số nguyên (5 < n < 20).
def taolist():
    n = int(input("Nhap so luong phan tu chua cac so nguyen (5 < n < 20):"))
    if not (5<n<20):
        raise ValueError("Số phần tử phải nằm trong khoảng 5 < n < 20.")

    lst = []
    print(f"Nhap {n} so nguyen:")
    for i in range (n):
        num = int(input(f"So thu {i+1}:"))
        lst.append(num)
    return lst
# 2. Số chẵn nào trong list xuất hiện nhiều nhất.
def max_sochan(lst):
    chan = [x for x in lst if x % 2 == 0]
    if not chan:
        return None
    return max(chan, key = chan.count)
# 3. Đưa ra các số lẻ nhỏ nhất có trong danh sách
def min_sole(lst):
    le = [x for x in lst if x % 2 != 0]
    if not le:
        return None
    return min(le)
# 4. Thay thế tất cả các số chia hết cho 5 trong danh sách thành số 5
def thay_chia5_thanh5(lst):
    return [5 if x%5==0 else x for x in lst ]
# 5. Số nào trong list xuất hiện nhiều nhất.
def so_xuathienmax(lst):
    return max(lst,key = lst.count)
# 6. Đưa ra các số lẻ nhỏ nhất có trong danh sách
def ht_sole_min(lst):
    sole = [x for x in lst if x % 2 != 0]
    return min(sole)
# 7. Xóa tất cả các số chia hết cho 3 có trong danh sách
def xoa_sochiahet3(lst):
    return [x for x in lst if x%3 !=0 ]