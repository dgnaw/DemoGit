# 1. Nhập 1 xâu ký tự s
def nhap_xau():
    return input("Nhap xau ky tu:")
# 2. Loại bỏ các ký tự trùng lặp trong xâu ký tự s.
def xoa_kytulap(s):
    return ''.join(sorted(set(s),key = s.index))
# 3. Đưa các xâu con của xâu s ra màn hình
def ht_xaucon(s):
    print("Xau con:")
    n = len(s)
    for i in range(n):
        for j in range (i+1,n+1):
            print(s[i:j])
# 4. Tìm xâu con dài nhất không chứa các ký tự trùng lặp trong một xâu
def longest_unique_substring(s):
    n = len(s)
    start = 0
    max_len = 0
    max_substr = ""
    seen_chars = set()  # Sử dụng set để theo dõi các ký tự đã gặp

    for end in range(n):
        # Nếu ký tự tại end đã xuất hiện, dịch chuyển start
        while s[end] in seen_chars:
            seen_chars.remove(s[start])  # Loại bỏ ký tự tại start
            start += 1
        seen_chars.add(s[end])  # Thêm ký tự mới vào set

        # Cập nhật xâu con dài nhất
        current_len = end - start + 1
        if current_len > max_len:
            max_len = current_len
            max_substr = s[start:end + 1]

    return max_substr
