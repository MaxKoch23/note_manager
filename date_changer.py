# Импортируем модуль datetime для работы с датами

from datetime import datetime


def get_valid_date(prompt):
    # Функция get_valid_date используется для запроса корректной даты у пользователя
    while True:
        try:
            date_str = input(prompt) # Запрашиваем ввод даты
           #Пробуем преобразовать строку в объект datetime
            valid_date = datetime.strptime(date_str, "%d-%m-%Y")
            return valid_date #Возвращаем объект datetime, если ввод корректен
        except ValueError:
            # Если формат некорректный, сообщаем об ошибке и повторяем ввод
            print("Ошибка: Введите дату в формате 'день-месяц-год', например, 15-12-2024.")

# Запрашиваем информацию у пользователя

username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")

# Используем функцию get_valid_date для ввода дат

created_date_obj = get_valid_date("Введите дату создания заметки (день-месяц-год): ")
issue_date_obj = get_valid_date("Ведите дату истечения заметки (день-месяц-год): ")

# Форматируем даты для вывода (без года)

formatted_created_date = created_date_obj.strftime("%d-%m")
formatted_issue_date = issue_date_obj.strftime("%d-%m")

# Выводим все данные на экран
print("\nВы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки", title)
print("Описание заметки:", content)
print("Статус заметки:", status)
print("Дата создания заметки:", formatted_created_date)
print("Дата истечения заметки:", formatted_issue_date)