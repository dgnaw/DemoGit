# 1. Nhập thông tin tên và tuổi của n cán bộ (0<n<20) vào một dictionarie
def nhap_tt():
    canbo = {}
    n = int(input("Nhap so luong can bo ( 0<n<20):"))
    while n <= 0 or n >= 20:
        n = int(input("Nhap lai so luong can bo ( 0<n<20):"))
    for i in range(n):
        name = input(f"Nhap ten can bo thu {i+1}:")
        age = int(input(f"Nhap tuoi can bo thu {i+1}:"))
        canbo[name] = age
    return canbo
# 2. Cán bộ nào nhiều tuổi nhất?
def max_age(canbo):
    max_tuoi = max(canbo.values())
    return [name for name,age in canbo.items() if age == max_tuoi]
# 3. Độ tuổi trung bình là bao nhiêu?
def tuoi_trungbinh(canbo):
    return sum(canbo.values()) / len(canbo)
# 4. Xóa đi những cán bộ có tuổi >40
def xoa_tuoi_hon40(canbo):
    age_canbo = {}
    for name,age in canbo.items():
        if age < 40:
            age_canbo[name] = age
    return age_canbo