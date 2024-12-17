import d10
phonebook = {}

while True:
    print("\nChọn chức năng:")
    print("1. Thêm 15 người dùng vào danh bạ")
    print("2. Hiển thị tổng số người có trong danh bạ")
    print("3. Tìm số điện thoại theo tên")
    print("4. Tìm tên theo chuỗi số trong số điện thoại")
    print("5. Thoát")

    choice = input("Lựa chọn của bạn: ").strip()

    if choice == "1":
        d10.add_contacts(phonebook)
    elif choice == "2":
        d10.display_total_contacts(phonebook)
    elif choice == "3":
        name = input("Nhập tên cần tìm: ").strip()
        d10.find_phone_by_name(phonebook, name)
    elif choice == "4":
        phone_fragment = input("Nhập chuỗi số cần tìm trong số điện thoại: ").strip()
        d10.find_names_by_phone_fragment(phonebook, phone_fragment)
    elif choice == "5":
        print("Thoát chương trình.")
        break
    else:
        print("Lựa chọn không hợp lệ. Vui lòng thử lại!")