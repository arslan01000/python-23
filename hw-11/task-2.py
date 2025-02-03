num1 = float(input("Enter first number: \n"))
num2 = float(input("Enter second number: \n"))

if num1 % 2 == 0 and num2 > 0:
    if num1 > num2:
        difference = num1 - num2
        print("The first number is greater than the second by", difference)
    elif num2 > num1:
        difference = num2 - num1
        print("The second number is greater than the first by", difference)
    else:
        print("Numbers are equal.")
else:
    print("Error")
