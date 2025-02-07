string = input("Введите строку: \n").strip()

if string:
    string = string.lower()
    
    length = len(string)
    
    first_char = string[0]
    
    last_char = string[-1]

    print(f"{'Длина строки':<20}{length}")
    print(f"{'Первый символ':<20}{first_char}")
    print(f"{'Последний символ':<20}{last_char}")
    
else:
    print("Вы ввели пустую строку. Error. \n")
