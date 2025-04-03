import hashlib

def sha256_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode('utf-8'))
    return sha256.hexdigest()

input_data = input("Nhập dữ liệu cần băm: ")
hash_value = sha256_hash(input_data)
print(f"Giá trị băm SHA-256: {hash_value}")