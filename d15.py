# 1. Nhập vào một dãy số nguyên cho tới khi không muốn nhập nữa. In dãy vừa nhập ra
# màn hình
def tao_ds():
    lst = []
    while True:
        try:
            n = int(input("Nhap so nguyen (nhan 'enter' de dung):"))
            lst.append(n)
        except ValueError:
            break
    return lst
# 2. Tìm phần tử nhỏ nhất trong các số chẵn có trong danh sách.
def min_chan(ds):
    sochan = [x for x in ds if x % 2 == 0]
    return min(sochan)
# 3. Xóa số đầu tiên trong danh sách.
def xoa_sodau(ds):
    if ds:
        del ds[0]
    return ds
# 4. Đếm số nguyên tố trong danh sách.
def dem_snt(ds):
    def snt(numbers):
        if numbers < 2:
            return False
        for i in range (2,int(numbers ** 0.5)+1):
            if numbers % i == 0:
                return False
        return True
    return sum(1 for num in ds if snt(num))