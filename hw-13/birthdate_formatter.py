# Converts a birthdate from DD/MM/YYYY format into a readable text format.

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

date_of_birth = input("Enter your birthdate in DD/MM/YYYY format: \n")

day, month, year = date_of_birth.split('/')

day = int(day)
month = int(month)

print(f"You were born in {year}, {day} {months[month - 1]}.")
