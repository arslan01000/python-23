# Multiplication table for 5 and full tables from 1 to 9

for i in range(1, 10):
    print(f"5 * {i} = {5 * i}")


#from 1 to 9
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")
    print()
