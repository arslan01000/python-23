def main():
    print("Enter 10 numbers: ")
    numbers = []
    
    for _ in range(10):
        num = float(input("> "))
        numbers.append(num)

    valid_commands = {"avg", "min", "max"}
    command = ""

    while command not in valid_commands:
        command = input("\nInput one of the commands (avg, min, max): \n> ").strip().lower()
        if command not in valid_commands:
            print("Invalid command!")


    if command == "avg":
        result = sum(numbers) / len(numbers)
    elif command == "min":
        result = min(numbers)
    elif command == "max":
        result = max(numbers)

    print(result) 

if __name__ == "__main__":
    main()
