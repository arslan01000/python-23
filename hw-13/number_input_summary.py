# Collects user-inputted numbers, calculates the total and average.

nums = []

print("Enter numbers:")

while True:
    user_input = input()
    if user_input == "end":
        break
    nums.append(int(user_input))

print("\nYou entered:", ", ".join(map(str, nums)))

total = sum(nums)
average = total / len(nums) if nums else 0

print(f"\nTotal: {total}")
print(f"\nAverage: {average:.1f}")
