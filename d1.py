# 1.Nhập vào một dãy số nguyên cách nhau bằng dấu phẩy,
# chuyển đổi chúng thành một danh sách các số nguyên.
import math
def convert_to_list(input_string):
    return list(map(int,input_string.split(',')))
# map(): dùng để chuyển đổi dữ liệu (ví dụ chuyển đổi từ chuỗi thành danh sách các số nguyên)
# 2. Tinh tong va tbc cac so trong danh sach
def tongvatbc(numbers):
    total = sum(numbers)
    average = sum(numbers) / len(numbers) if numbers else 0
    return total,average
# 3.Tim vi tri phan tu am dau tien va am cuoi
def amdau_amcuoi(numbers):
    first_neg = next((i for i, x in enumerate(numbers) if x<0),None)
    end_neg = next((i for i, x in reversed(list(enumerate(numbers))) if x<0),None)
    return first_neg, end_neg
#next(): dùng để in ra phần tử đầu tiên nếu thỏa mãn điều kiện nếu mà không có sẽ hiện None
#enumerate(): dùng để duyệt qua các phần tử của iterable(chuỗi,danh sách,tuple)
# 4. Dua ra so luong cac so duong lien tiep
def duong_lientiep(numbers):
    max_count = count = 0
    for num in numbers:
        if num > 0 :
            count+=1
        else:
            max_count = max(max_count,count)
            count = 0
    return max(max_count,count)
# 5.Danh sach cac so chan trong day so nguyen
def dayso_chan(numbers):
    return [x for x in numbers if x%2 ==0]
# 6.Danh sach cac so le trong day
def dayso_le(numbers):
    return [x for x in numbers if x % 2 !=0]
# 7.Tim phan tu lon nhat va vi tri lon nhat cuoi cung
def max_maxend(numbers):
    number_max = max(numbers)
    number_end_max = len(numbers) - 1 - numbers[::-1].index(number_max)
    return number_max,number_end_max
# 8. Loai bo cac gia tri trung nhau
def gt_trung(numbers):
    # return list(set(numbers))
    return list(dict.fromkeys(numbers))
# Có thể dùng cả set và cả dict
# 9. Sap xep theo tang dan
def sx_tang(numbers):
    return sorted(numbers)
# 10. Nhap x. Chen x vao danh sach sao cho day tang
def chenx_tangdan(numbers,x):
    for i,num in enumerate(numbers):
        if x < num:
            return numbers[:i] + [x] + numbers[i:]
    return numbers + [x]
# 11.Hien thi So chinh phuong trong danh sach
def hienthi_scp(numbers):
    squares = []
    for num in numbers:
        root = math.sqrt(num)
        if root * root == num:
            squares.append(num)
    return squares
# 12. So luong phan tu dan dau dai nhat
def sl_dandau_dainhat(numbers):
    max_len = curr_len = 1
    for i in range(1, len(numbers)):
        if numbers[i] * numbers[i - 1] < 0:
            curr_len += 1
            max_len = max(max_len, curr_len)
        else:
            curr_len = 1
    return max_len
# 13. Co bao nhieu so chinh phuong
def dem_scp(numbers):
    return sum(1 for x in numbers if int(math.sqrt(x))**2 == x)
# 14. Sap xep giam dan
def sx_giam(numbers):
    return sorted(numbers, reverse = True)
# 15. Nhap so nguyen k, xoa phan tu thu k trong danh sach
def xoa_k(numbers,k):
    if 0<= k < len(numbers):
        return numbers[:k] + numbers[k + 1:]
    return numbers
# 16.Trong danh sach co bao nhieu so bi lap
def solap(numbers):
    return sum(count > 1 for count in {x: numbers.count(x) for x in set(numbers)}.values())
# 17. Dao nguoc thu tu danh sach
def dao_thutu(numbers):
    return numbers[::-1]
# 18. Tim so nguyen to va in ra man hinh
def snt(numbers):
    def is_snt(n):
        if n<2:
            return False
        for i in range (2,int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True
    return [x for x in numbers if is_snt(x)]
# 19.Nhap x va kiem tra x co trong danh sach chua . Neu chua thi them x vao
def ktrax_danhsach(numbers,x):
    if x not in numbers:
        numbers.append(x)
    return numbers