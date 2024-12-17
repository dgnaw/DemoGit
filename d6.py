# 1. Nhập một tuple chứa n số nguyên (5<n<30)
def nhap_tuple():
    while True:
            n = int(input("Nhap so luong phan tu cua tuple (5<n<30):"))
            if 5 < n < 30:
                break
            else:
                n = int(input("Nhap so luong phan tu cua tuple (5<n<30):"))
    return tuple(int(input(f"Nhap so thu {i+1}:"))for i in range (n))
# 2. Đưa ra màn hình trung bình cộng các số có trong tuple vừa nhập
def hienthi_tbc(tup):
    return sum(tup) / len(tup)
# 3. Nhập một số X từ bàn phím. Chèn X vào tuple vừa nhập
def chenx_vaotuple(tup,x):
#Cach 1:
    return tup + (x,)
#Cach 2:
# lst = list(tup)
    # lst.append(x)
    # return tuple(lst)
# 4. Đưa ra màn hình các số hoàn hảo có trong tuple
def shh(num):
    if num < 1:
        return False
    return sum(i for i in range (1,num) if num % i ==0) == num
# 5. Đưa ra màn hình các số nguyên tố có trong tuple
def snt(num):
    if num < 2:
        return False
    for i in range (2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
# 6. Đưa ra màn hình tổng các số có trong tuple vừa nhập
def tong(tup):
    return sum(tup)