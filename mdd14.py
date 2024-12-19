import d14
input_string = input("Nhap so nguyen cach nhau bang dau phay:")
ds = d14.tao_danhsach(input_string)
print("Danh sach:",ds)
# d14.sochan_sole(ds)
print("So luong so am lien tiep it nhat:",d14.soam_lientiep(ds))
print("Tong va trung binh cong : ",d14.tongvatbc(ds))