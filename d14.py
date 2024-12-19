# 1. Nhập vào một dãy số nguyên cách nhau bằng dấu phẩy, chuyển đổi chúng thành một
# danh sách các số nguyên.
def tao_danhsach(input_string):
    return list(map(int,input_string.split(',')))
# 2. Đưa các số chẵn trên một dòng, các số lẻ trên một dòng.
def sochan_sole(ds):
    sochan = [x for x in ds if x % 2 == 0]
    sole = [x for x in ds if x % 2 != 0]
    print("So chan:",sochan)
    print("So le:",sole)
# 3. Đưa ra số lượng các số âm liên tiếp ít nhất
def soam_lientiep(ds):
    count = 0
    min_streak = float('inf')
    for num in ds:
        if num < 0:
            count+=1
        else:
            if count > 0:
                min_streak = min(min_streak,count)
            count = 0
    if count > 0:
        min_streak = min(min_streak,count)
    return min_streak if min_streak != float ('inf') else 0
# 4. Đưa ra tổng và trung bình cộng các phần tử trong danh sách
def tongvatbc(ds):
    tong = sum(ds)
    tbc = sum(ds) / len(ds)
    return tong,tbc