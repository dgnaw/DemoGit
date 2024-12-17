def add_contacts(phonebook):
    """Thêm 15 liên lạc vào danh bạ."""
    print("Nhập thông tin 15 người dùng:")
    for i in range(15):
        name = input(f"Nhập họ tên người thứ {i+1}: ").strip()
        phone = input(f"Nhập số điện thoại của {name}: ").strip()
        phonebook[name] = phone
    print("Đã thêm 15 người vào danh bạ.")

def display_total_contacts(phonebook):
    """Hiển thị tổng số người có trong danh bạ."""
    print(f"Tổng số người trong danh bạ: {len(phonebook)}")

def find_phone_by_name(phonebook, name):
    """Tìm số điện thoại của người có tên vừa nhập."""
    phone = phonebook.get(name)
    if phone:
        print(f"Số điện thoại của {name}: {phone}")
    else:
        print(f"Không tìm thấy tên '{name}' trong danh bạ.")

def find_names_by_phone_fragment(phonebook, phone_fragment):
    """Tìm tất cả những người có số điện thoại chứa chuỗi số vừa nhập."""
    print(f"Kết quả tìm kiếm với chuỗi số '{phone_fragment}':")
    found = False
    for name, phone in phonebook.items():
        if phone_fragment in phone:
            print(f"{name}: {phone}")
            found = True
    if not found:
        print("Không tìm thấy số điện thoại phù hợp.")
