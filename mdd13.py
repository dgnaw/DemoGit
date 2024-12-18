import d13
student_names = input("Nhập danh sách học sinh (cách nhau bằng dấu phẩy): ")
students_list = d13.convert_to_list(student_names)
print("Học sinh có tên dài nhất:", d13.longest_name(students_list))
print("Học sinh có tên ngắn nhất:", d13.shortest_name(students_list))
print("Danh sách học sinh theo thứ tự alphabet:", d13.sort_alphabetically(students_list))
students_list = d13.remove_duplicates(students_list)
print("Danh sách học sinh sau khi loại bỏ tên trùng:", students_list)