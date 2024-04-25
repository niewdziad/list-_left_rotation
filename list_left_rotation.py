def left_rotate(l, num):
    return l[num:] + l[:num]

# Testy:
list_ = list("1234567")
print(left_rotate(list_, 4))  # Powinno zwrócić ["5", "6", "7", "1", "2", "3", "4"]
print(left_rotate(list_, 5) is not list_)  # Powinno być True