# 1. Nhập vào một dãy số nguyên cách nhau bằng dấu phẩy, chuyển đổi chúng thành một
# danh sách các số nguyên lưu chúng vào một tuple
def tao_tuple(nhap_so):
    return tuple(map(int,nhap_so.split(',')))
# 2. In một nửa số giá trị đầu tiên của tuple trong 1 dòng và 1 nửa số giá trị cuối trong 1
# dòng.
def nuagiatri_tuple(tup):
    n = len(tup)
    nuadau = n // 2
    nuasau = n // 2
    print("Nua dau tuple:",tup[:nuadau])
    print("Nua sau tuple:",tup[nuasau:])
# 3. Tạo ra và in tuple chứa các số chẵn được lấy từ tuple
def sochan(tup):
    sochan = [x for x in tup if x % 2 == 0]
    return tuple(sochan)
# 4. Trong tuple có bao nhiêu số trùng lặp
def sotrunglap(tup):
    return sum(count > 1 for count in {x: tup.count(x) for x in set(tup)}.values())