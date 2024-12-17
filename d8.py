# 1. Nhập thông tin của học sinh đến khi không muốn nhập nữa. Thông tin bao gồm: Điểm, tên
# của học sinh và lưu thông tin này trong một từ điển gọi là myclass. Điểm sẽ thuộc trong tập
# hợp 0,1,2,…,10. Tên là một chuỗi ký tự nhập vào.
def nhap_hocsinh(myclass):
    while True:
        name = input("Nhap ten hoc sinh ( go exit de dung):")
        if name.lower() == "exit":
            break
        score = int(input("Nhap so diem cua hoc sinh ( tu 0 den 10):"))
        if score < 0 or score > 10:
            score = int(input("Vui long nhap lai ( tu 0 den 10):"))
            continue
        myclass[name] = score
# 2. Thống kê số học sinh được điểm 10, điểm 9, điểm 8.…
def thongke_diem(myclass):
    score_stats = {i: 0 for i in range (11)}
    for score in myclass.values():
        score_stats[score]+=1
    return score_stats
# 3. Có bao nhiêu học sinh có điểm giỏi (điểm >=7)
def dem_hsg(myclass):
    return sum(1 for score in myclass.values() if score >= 7)
# 4. Xóa học sinh ‘ Huệ Chi’ khỏi danh sách.
def xoahs(myclass,name):
    if name in myclass:
        del myclass[name]
        print(f"Da xoa hoc sinh {name} khoi danh sach")
    else:
        print(f"Danh sach khong co ten {name}")