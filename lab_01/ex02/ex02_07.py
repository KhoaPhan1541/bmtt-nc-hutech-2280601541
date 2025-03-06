print("Nhập các dòng văn bản (Nhập 'done' để kết thúc):")

lines = []  # Khởi tạo danh sách để lưu các dòng

while True:
    line = input()  # Nhận dòng văn bản từ người dùng
    if line.lower() == 'done':  # Kiểm tra nếu người dùng nhập 'done'
        break  # Thoát khỏi vòng lặp
    lines.append(line)  # Thêm dòng vào danh sách

# Chuyển các dòng thành chữ in hoa và in ra màn hình
print("\nCác dòng đã nhập sau khi chuyển thành chữ in hoa:")
for line in lines:
    print(line.upper())  # In ra dòng văn bản dưới dạng chữ in hoa
