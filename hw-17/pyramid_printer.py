def get_valid_height():
    while True:
        try:
            height = int(input("Input pyramid height:\n> "))
            if height > 0:
                return height
            else:
                print("Error: Height must be a positive integer. Try again.")
        except ValueError:
            print("Error: Please enter a valid integer.")

def print_pyramid(height):
    print("\nYour pyramid sir:\n")
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))

if __name__ == "__main__":
    height = get_valid_height()
    print_pyramid(height)
