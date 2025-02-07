import random

statistic_list = [True, False, False, False, True, False]

num1 = random.randint(1, 9)
num2 = random.randint(1, 9)

user_answer = int(input(f"Сколько будет {num1} * {num2}? \n"))

correct_answer = num1 * num2

if user_answer == correct_answer:
    is_correct = True
else:
    is_correct = False

statistic_list.append(is_correct)

correct_count = statistic_list.count(True)
incorrect_count = statistic_list.count(False)
total_count = len(statistic_list)
percentage = (correct_count / total_count) * 100

print(f"{'Правильных ответов:':<35}{correct_count}")
print(f"{'Неправильных ответов:':<35}{incorrect_count}")
print(f"{'Процент правильных ответов:':<35}{percentage:.2f}%")
