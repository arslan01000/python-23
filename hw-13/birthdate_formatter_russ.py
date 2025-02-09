months = ["января", "февраля", "марта", "апреля", "мая", "июня","июля", "августа", "сентября", "октября", "ноября", "декабря"]

date_of_birth = input("Введите дату рождения в формате ДД/ММ/ГГГГ: \n")

day, month, year = date_of_birth.split('/')

day = int(day)
month = int(month)

print(f"Вы родились в {year} году, {day} {months[month - 1]}.")
