# 1. Nhập các khoản chi tiêu hằng ngày trong một tuần vào một dictionarie với ngày là
# key, số tiền chi tiêu trong ngày tương ứng là value
def tao_dict():
    chitieu = {}
    for day in ["Thu 2","Thu 3","Thu 4","Thu 5","Thu 6","Thu 7","Chu nhat"]:
        chitieu[day] = float(input(f"Nhap so tien chi tieu cho {day}:"))
    return chitieu
# 2. Tính tổng chi tiêu, chi tiêu trung bình mỗi ngày
def tongvatbc_chitieu(chitieu):
    tong = sum(chitieu.values())
    tbc = tong / len(chitieu)
    print(f"Tong chi tieu moi ngay la {tong}")
    print(f"Trung binh cong chi tieu la {tbc}")
# 3. Tìm ra ngày chi tiêu nhiều nhất và ít nhất.
def max_min_chitieu_ngay(chitieu):
    max_day = max(chitieu,key = chitieu.get)
    min_day = min(chitieu,key = chitieu.get)
    return max_day,chitieu[max_day],min_day,chitieu[min_day]
# 4. Loại thông tin chi tiêu ngày cuối cùng
def loai_chitieu_ngaycuoi(chitieu):
    chitieu.popitem()
    return chitieu