# Analyzes a user-input string: length, first, and last character

string = input("Enter a string: \n").strip()

if string:
    string = string.lower()
    
    length = len(string)
    
    first_char = string[0]
    
    last_char = string[-1]

    print(f"{'String length':<20}{length}")
    print(f"{'First character':<20}{first_char}")
    print(f"{'Last character':<20}{last_char}")
    
else:
    print("You entered an empty string. Error. \n")
