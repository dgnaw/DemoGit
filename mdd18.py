import d18
chitieu = d18.tao_dict()
print("Hien thi:")
for day,money in chitieu.items():
    print(f"{day}:{money}")
d18.tongvatbc_chitieu(chitieu)
print("Hien thi:",d18.max_min_chitieu_ngay(chitieu))
print("Sau khi loai bo ngay cuoi cung:",d18.loai_chitieu_ngaycuoi(chitieu))