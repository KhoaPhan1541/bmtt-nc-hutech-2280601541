def tao_tuple_tu_list (lst):
    return tuple(lst)

input_list = input("nhập danh sách các số, cách nhau bằng dấu phẩy: ")
numbers = list(map(int, input_list.split(',')))

my_tuple = tao_tuple_tu_list(numbers)
print("list: ", numbers)
print("tuple từ List:", my_tuple)
