# Создаем словарь для хранения статусов заметки

note = {1: "Выполнено",
        2: "В процессе",
        3: "Отложено",
        4: "Другое (введите свой статус)"}

# Выводим текущий статус
current_status = note[2]
print(f"\nТекущий статус заметки: {current_status}")

# Выводим список возможных статусов
print("\nВыберите новый статус заметки:")
for key, value in note.items():
    print(f"{key}. {value}")

# Получение ввода
while True:
    user_input = input("\nВведите номер своего статуса: ").strip()

    # Проверка ввода
    if user_input.isdigit() and int(user_input) in note:
        user_choice = int(user_input)

        # Если пользователь выбрал опцию "другое"
        if user_choice == 4:
            new_status = input("Введите новый статус: ").strip()

            # Проверяем, что строка не пустая и не слишком длинная
            if new_status and len(new_status)<=50:
                current_status = new_status
                break
            else:
                print("Статус должен быть не пустым и не длиннее 50 символов. Попробуйте снова.")
        else:
            current_status = note[user_choice]
            break
    else:
        print("Некорректный ввод. Пожалуйста, выберите из предложенных вариантов.")

# Вывод обновленного статуса
print(f"\nСтатус заметки успешно обновлён на: {current_status}")


