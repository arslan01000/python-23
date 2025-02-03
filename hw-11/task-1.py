import datetime

first_name = input("Enter your name: \n").capitalize()
last_name = input("Enter your last name: \n").capitalize()
birth_year = int(input("When were you born? \n"))
country = input("Where are you from? \n").capitalize()

current_year = datetime.datetime.now().year
age = current_year - birth_year

print(first_name, last_name + ".", "You are", age, "years old.", "You are living in", country + ".")
