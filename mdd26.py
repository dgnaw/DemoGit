import d26
s = input("Nhap xau s:")
print("Xau dao nguoc:",d26.nhap_xau(s))
print("Tat ca xau con:",d26.ht_tatca_xaucon(s))
print("Ky tu xuat hien nhieu nhat:",d26.kytu_max(s))
print("Xau sau khi xoa ky tu trung:",d26.xoa_trung(s))
nguyenam,phuam,kt = d26.songuyenam_phuam_khoangtrang(s)
print(f"Nguyen am:{nguyenam},Phu am:{phuam},Khoang trang:{kt}")
print("Kiem tra xau co so nguyen duong khong ?:",d26.xau_soduong(s))
x = input("Nhap x:")
print("Xoa ky tu x ra khoi xau:",d26.xoa_kytux(s,x))