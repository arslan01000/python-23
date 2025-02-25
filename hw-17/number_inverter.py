def invert_number(num):
    return 0 - num

numbers = [1, -2, 5, 2.5, -4]

inverted_numbers = [invert_number(n) for n in numbers]

print("before invert:", numbers)
print("after invert:", inverted_numbers)
