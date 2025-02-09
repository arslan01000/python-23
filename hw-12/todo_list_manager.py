todo_list = ['Вынести мусор', 'Погулять с собакой', 'Оплатить интернет']

todo_list_sorted = sorted(todo_list)
print("\nВаш список дел:")

if len(todo_list_sorted) > 0:
    print(f"1. {todo_list_sorted[0]}")
if len(todo_list_sorted) > 1:
    print(f"2. {todo_list_sorted[1]}")
if len(todo_list_sorted) > 2:
    print(f"3. {todo_list_sorted[2]}")
if len(todo_list_sorted) > 3:
    print(f"4. {todo_list_sorted[3]}")
if len(todo_list_sorted) > 4:
    print(f"5. {todo_list_sorted[4]}")

action = input("\nВыберите действие: добавить (1), удалить (2) или выйти (3): ").strip()

if action == "1":
    new_task = input("Введите новое дело: ").strip().capitalize()

    match new_task.lower():
        case task if len(todo_list) > 0 and task == todo_list[0].lower():
            print("Такое дело уже есть в списке!")
        case task if len(todo_list) > 1 and task == todo_list[1].lower():
            print("Такое дело уже есть в списке!")
        case task if len(todo_list) > 2 and task == todo_list[2].lower():
            print("Такое дело уже есть в списке!")
        case task if len(todo_list) > 3 and task == todo_list[3].lower():
            print("Такое дело уже есть в списке!")
        case task if len(todo_list) > 4 and task == todo_list[4].lower():
            print("Такое дело уже есть в списке!")
        case _:
            todo_list.append(new_task)
            print(f"Дело '{new_task}' добавлено в список!")
        
    todo_list_sorted = sorted(todo_list)
    print("\nВаш список дел:")
    if len(todo_list_sorted) > 0:
        print(f"1. {todo_list_sorted[0]}")
    if len(todo_list_sorted) > 1:
        print(f"2. {todo_list_sorted[1]}")
    if len(todo_list_sorted) > 2:
        print(f"3. {todo_list_sorted[2]}")
    if len(todo_list_sorted) > 3:
        print(f"4. {todo_list_sorted[3]}")
    if len(todo_list_sorted) > 4:
        print(f"5. {todo_list_sorted[4]}")

elif action == "2":
    task_number = int(input("Введите номер дела для удаления: "))
    todo_list_sorted = sorted(todo_list)

    if task_number == 1 and len(todo_list_sorted) > 0:
        todo_list.remove(todo_list_sorted[0])
    elif task_number == 2 and len(todo_list_sorted) > 1:
        todo_list.remove(todo_list_sorted[1])
    elif task_number == 3 and len(todo_list_sorted) > 2:
        todo_list.remove(todo_list_sorted[2])
    elif task_number == 4 and len(todo_list_sorted) > 3:
        todo_list.remove(todo_list_sorted[3])
    elif task_number == 5 and len(todo_list_sorted) > 4:
        todo_list.remove(todo_list_sorted[4])
    else:
        print("Некорректный номер! Попробуйте снова.")

    todo_list_sorted = sorted(todo_list)
    print("\nВаш список дел:")
    if len(todo_list_sorted) > 0:
        print(f"1. {todo_list_sorted[0]}")
    if len(todo_list_sorted) > 1:
        print(f"2. {todo_list_sorted[1]}")
    if len(todo_list_sorted) > 2:
        print(f"3. {todo_list_sorted[2]}")
    if len(todo_list_sorted) > 3:
        print(f"4. {todo_list_sorted[3]}")
    if len(todo_list_sorted) > 4:
        print(f"5. {todo_list_sorted[4]}")

elif action == "3":
    print("Выход из программы. До свидания!")

else:
    print("Неверный ввод. Программа завершена.")
