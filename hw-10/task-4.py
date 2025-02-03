import math

jake_score = int(input("Введите оценку Джейку: \n"))
john_score = int(input("Введите оценку для Джона: \n"))
jack_score = int(input("Введите оценку для Джека: \n"))
jane_score = int(input("Введите оценку Джейн: \n"))
result = math.ceil((jake_score + john_score + jack_score + jane_score) / 4)
print("Среднее по оценкам:", result)
