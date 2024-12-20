# Импортируем модуль datetime для работы с датами

from datetime import datetime

def get_valid_date(prompt):
    # Функция get_valid_date используется для запроса корректной даты у пользователя
    while True:
        try:
            date_str = input(prompt) # Запрашиваем ввод даты
           # Пробуем преобразовать строку в объект datetime
            valid_date = datetime.strptime(date_str, "%d-%m-%Y")
            return valid_date #Возвращаем объект datetime, если ввод корректен
        except ValueError:
            # Если формат некорректный, сообщаем об ошибке и повторяем ввод
            print("Ошибка: Введите дату в формате 'день-месяц-год', например, 15-12-2024.")


    # Функция get_titles запрашивает количество заголовков у пользователя
def get_titles():
    titles = [] # Создаем пустой список для хранения заголовков
    count = int(input("Сколько заголовков вы хотите добавить?: ")) # Запрашиваем количество заголовков

    # Используем цикл для ввода заголовков
    for i in range(1, count + 1):
        title = input(f"Введите заголовок {i}: ") # Запрашиваем заголовок
        titles.append(title) # Добавляем заголовок в конец списка

    return titles # Возвращаем список заголовков

# Основной код программы
print("Добро пожаловать в программу для управления заметками!\n")

# Создаем словарь для хранения информации о заметке
note = {}

# Сбор данных от пользователя
note["username"] = input("Введите имя пользователя: ")
note["content"] = input("Введите описание заметки: ")
note["status"] = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")

# Обработка даты создания
note["created_date"] = get_valid_date("Введите дату создания заметки (день-месяц-год): ")

# Обработка даты истечения
note["issue_date"] = get_valid_date("Ведите дату истечения заметки (день-месяц-год): ")

# Получение заголовков с помощью функции
note["titles"] = get_titles()

# Выводим собранные данные
print("\nСобранная информация о заметке:")
for key, value in note.items():
    # Если ключ – даты, выводим их в нужном формате (без года)
    if key in ["created_date", "issue_date"]:
        print(f"{key.capitalize()}: {value.strftime('%d-%m')}")
    else:
        print(f"{key.capitalize()}: {value}")
