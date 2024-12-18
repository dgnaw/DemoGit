# 1. Nhập vào một dãy họ tên các học sinh cách nhau bởi dấu phẩy, chuyển đổi chúng
# thành một list họ tên học sinh .
def convert_to_list(names: str):
    return names.split(',')

# 2.Đưa ra học sinh có tên dài nhất
def longest_name(names_list):
    max_length = max(len(name) for name in names_list)
    return [name for name in names_list if len(name) == max_length]

# 3.Đưa ra học sinh có tên ngắn nhất
def shortest_name(names_list):
    min_length = min(len(name) for name in names_list)
    return [name for name in names_list if len(name) == min_length]

# 4.Đưa ra danh sách họ tên học sinh theo Anphabet
def sort_alphabetically(names_list):
    return sorted(names_list)

# 5.Có họ tên nào bị lặp trong danh sách không? Nếu có loại tên trùng đó khỏi danh sách.
def remove_duplicates(names_list):
    return list(set(names_list))

