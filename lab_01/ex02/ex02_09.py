def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False  # Nếu n <= 1, không phải số nguyên tố
    for i in range(2, int(n**0.5) + 1):  # Kiểm tra chia hết từ 2 đến căn bậc hai của n
        if n % i == 0:  # Nếu n chia hết cho i, n không phải số nguyên tố
            return False
    return True  # Nếu không chia hết cho bất kỳ số nào, n là số nguyên tố

# Kiểm tra số nguyên tố và in kết quả
number = int(input("Nhập vào số cần kiểm tra: "))

if kiem_tra_so_nguyen_to(number):
    print(number, "là số nguyên tố.")
else:
    print(number, "không phải là số nguyên tố.")
