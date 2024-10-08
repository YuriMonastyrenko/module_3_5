def get_multiplied_digits(number):
    str_number = str(int(number))
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result1 = get_multiplied_digits(40203)
result2 = get_multiplied_digits(100000000067088)
result3 = get_multiplied_digits("0092")
print(result1)
print(result2)
print(result3)
