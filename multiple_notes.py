from datetime import datetime


def get_non_empty_input(prompt):
    """Функция get_non_empty_input проверяет, что пользователь ввел непустую строку"""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Поле не может быть пустым. Попробуйте снова.")


def get_valid_date(prompt):
    # Функция get_valid_date используется для запроса корректной даты у пользователя
    while True:
        try:
            date_str = input(prompt)  # Запрашиваем ввод даты
            # Пробуем преобразовать строку в объект datetime
            valid_date = datetime.strptime(date_str, "%d-%m-%Y")
            return valid_date  # Возвращаем объект datetime, если ввод корректен
        except ValueError:
            # Если формат некорректный, сообщаем об ошибке и повторяем ввод
            print("Ошибка: Введите дату в формате 'день-месяц-год', например, 15-12-2024.")


def add_note(notes):
    """Добавляет новую заметку в список"""
    note_id = len(notes) + 1  # Генерация уникального ID
    print("\nДобро пожаловать в менеджер заметок! Вы можете добавить новую заметку.")
    username = get_non_empty_input("Введите имя пользователя: ")
    while True:
        title = get_non_empty_input("Введите заголовок заметки: ")
        if any(note['Заголовок'].lower() == title.lower() for note in notes):
            print("Заголовок уже существует. Попробуйте другой.")
        else:
            break

    content = input("Введите описание заметки: ").strip()
    status = get_non_empty_input("Введите статус заметки (например: новая, в процессе, выполнено): ")
    created_date = datetime.now().strftime("%d-%m-%Y")
    deadline = get_valid_date("Введите дату дедлайна (дд-мм-гггг): ")

     # Создание словаря для заметки
    note = {
        "ID": note_id,
        "Имя пользователя": username,
        "Заголовок": title,
        "Описание": content,
        "Статус": status,
        "Дата создания": created_date,
        "Дедлайн": deadline
    }
    notes.append(note)
    print(f"\nЗаметка с ID {note_id} успешно добавлена!")

# Функция для удаления заметки
def delete_note(notes):
    print("\nУдаление заметки:")
    note_id = input("Введите ID заметки для удаления: ").strip()
    for note in notes:
        if str(note["ID"]) == note_id:
            notes.remove(note)
            print(f"Заметка с ID {note_id} успешно удалена!")
            return
    print(f"Заметка с ID {note_id} не найдена.")

# Функция проверки уникальности заголовков


# Основной код
notes = []  # Список для хранения заметок
while True:
    print("\nМеню:")
    print("1. Добавить заметку")
    print("2. Удалить заметку")
    print("3. Показать все заметки")
    print("4. Выйти")
    choice = input("Выберите нужный пункт (1-4): ").strip()
    if choice == "1":
        add_note(notes)
    elif choice == "2":
        if notes:
            delete_note(notes)
        else:
            print("Нет заметок для удаления.")
    elif choice == "3":
        if notes:
            print("\nВсе заметки:")
            for note in notes:
                print("=" * 20)
                print(f"\nID: {note['ID']}")
                print(f"Имя пользователя: {note['Имя пользователя']}")
                print(f"Заголовок: {note['Заголовок']}")
                print(f"Описание: {note['Описание']}")
                print(f"Статус: {note['Статус']}")
                print(f"Дата создания: {note['Дата создания']}")
                print(f"Дедлайн: {note['Дедлайн']}")
        else:
            print("Список заметок пуст.")
    elif choice == "4":
        print("Выход из программы.")
        break
    else:
        print("Неверный ввод. Попробуйте снова.")



