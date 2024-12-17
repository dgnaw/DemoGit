# 1. Nhập một xâu ký tự s. In ra tất cả các ký tự trong xâu vừa nhập
def in_kytu(s):
    return list(s)
# 2. Đếm số lượng ký tự số trong xâu
def dem_kytu(s):
    return sum(c.isdigit() for c in s)
#isdigit(): dùng để kiểm tra xem một chuỗi có ký tự số không?
# 3. Đưa ra từ có nhiều ký tự nhất trong xâu ký tự (từ là các ký tự liền nhau không chứa dấu
# cách)?
def kytu_nhieu(s):
    words = s.split()
    return max(words,key = len) if words else ""
# 4. Nhập xâu s1, kiểm tra xem xâu s1 có phải là xâu con của xâu s không?
def kt_xaucon(s,s1):
    return s1 in s
# 5. Hiển thị tất cả các xâu con khác nhau của một xâu ký tự.
def ht_xaucon_khacnhau(s):
    sub_strings = set()
    for i in range (len(s)):
        for j in range (i+1,len(s) + 1):
            sub_strings.add(s[i:j])
    return list(sub_strings)
# 6. Xóa từ đầu tiên khỏi xâu (từ là các ký tự liền nhau không chứa dấu cách)
def xoa_tudau(s):
    words = s.split()
    return "".join(words[1:])
# 7. Chuyển đổi một xâu ký tự thành mã ASCII
def chuyendoi_ASCII(s):
    return [ord(c) for c in s]
# 8. Đưa ký tự có mã lớn nhất.
def ma_lonnhat(s):
    max_ASCII = max(s,key = ord)
    return max_ASCII if max_ASCII else ""
# 9. Đưa ra danh sách các từ có trong xâu ký tự theo độ dài của chúng tăng dần (từ là các ký tự
# liền nhau không chứa dấu cách)
def ds_dodai_tangdan(s):
    return sorted(s.split(),key = len)
# 10. Đếm số lượng ký tự đặc biệt trong một xâu ký tự (là các ký tự không phải ký tự số, không
# phải ký tự chữ cái in hoa hoặc chữ cái thường)
def Dem_kytudacbiet(s):
    return sum(not c.isalnum() for c in s)
#isalnum() : dùng để kiểm tra một ký tự hoặc 1 chuỗi có phải ký tự chữ hoặc số không ?
# 11. Tìm xâu con dài nhất chứa tất cả các ký tự trong một xâu ký tự.
def longest_unique_char_substring(s: str) -> str:
    seen = {}
    start = max_length = 0
    longest_substring = ""
    for i, c in enumerate(s):
        if c in seen and seen[c] >= start:
            start = seen[c] + 1
        seen[c] = i
        if i - start + 1 > max_length:
            max_length = i - start + 1
            longest_substring = s[start:i+1]
    return longest_substring
# 12. Nhập ký tự bất kỳ. Kiểm tra xem ký tự đó có trong một xâu không?
def kt_trongxau(s,s2):
    return s2 in s
# 13. Loại bỏ khoảng trắng thừa ở đầu và cuối xâu.
def bo_khoangtrong_daucuoi(s):
    return s.strip()
#strip(): dùng để loại bỏ ký tự khoảng trắng ở đầu và cuối
# 14. Nhập xâu s1 tìm tất cả các vị trí mà s1 xuất hiện trong xâu s.
def tim_vitris1(s,s1):
    position = []
    index = s.find(s1)
    while index != -1:
        position.append(index)
        index = s.find(s1,index+1)
    return position
# 15. Trong xâu s có bao nhiêu chữ hoa.
def kt_chuhoa(s):
    return sum(c.isupper() for c in s)
# 16. Chuyển tất cả các ký tự đầu mỗi từ thành chữ hoa
def chuyentudau_thanhhoa(s):
    return ''.join(word.capitalize() for word in s .split())
#capitalize():  sử dụng để chuyển đổi ký tự đầu tiên của một chuỗi thành chữ hoa và
# tất cả các ký tự còn lại thành chữ thường
# 17. Nhập ký tự C tìm tất cả các vị trí mà C xuất hiện trong xâu s.
def timvitri_Cxuathien(s,c):
    return [i for i, char in enumerate(s) if char == c]
# 18. Xóa tất cả các ký tự đặc biệt trong xâu chỉ giữ lại các chữ cái và số.
def xoa_ktdacbiet(s):
    return "".join(c for c in s if c.isalnum())
# 19. Tìm từ dài nhất trong chuỗi (từ là các ký tự liền nhau không chứa dấu cách)
def max_kytu(s):
    return max(s.split(),key = len) if s.split() else ""
# 20. Xóa từ đầu tiên khỏi chuỗi
def xoatu_dautien(s):
    return "".join(s.split()[1:])
# 21. Nhập chuỗi s1, ghép s, s1 để thành một chuỗi
def gheps_s1(s,s1):
    return s + s1