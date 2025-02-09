# Compares a selected number with other elements in a list and prints the results.

numbers = []
for i in range(3):
    num = int(input(f"Enter numeric value for {i + 1} element: \n"))
    numbers.append(num)

index = int(input("Enter key of element for comparison (0-2): \n"))

selected_value = numbers[index]

print("\nResult:")
for i in range(3):
    result = selected_value > numbers[i]
    print(f"{i + 1}) {selected_value} > {numbers[i]} = {result}")
