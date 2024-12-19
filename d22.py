# 1. Để quản lý từ vựng, người dùng có thể nhập một chuỗi các từ cách nhau bởi dấu phẩy.
def nhap_chuoi():
    chuoi = input("Nhap chuoi cach nhau boi dau phay:")
    return chuoi
# 2. Tách các từ trong chuỗi, sắp xếp chúng theo thứ tự bảng chữ cái.
def tach_sx_theoalpha(chuoi_tuvung):
    tach_chuoi = chuoi_tuvung.split(",")
    tach_chuoi = [t.strip() for t in tach_chuoi]
    return sorted(tach_chuoi)
# 3. Loại bỏ các từ trùng lặp.
def loaibo_trunglap(chuoi_tuvung):
    return sorted(set(chuoi_tuvung))
# 4. Đếm các từ có chứa các chữ số
def dem_chuso(chuoi_tuvung):
    return sum(1 for tach_chuoi in chuoi_tuvung if any(c.isdigit() for c in tach_chuoi))