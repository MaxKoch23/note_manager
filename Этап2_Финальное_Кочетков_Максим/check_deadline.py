"""
Файл: check_deadline.py
Описание:
- Содержит функциональность для обработки дедлайнов заметок.
- Позволяет пользователю сравнивать дату дедлайна с текущей датой.
- Информирует пользователя о состоянии дедлайна.

Функциональность:
1. Запрашивает дату дедлайна и сравнивает её с текущей датой.
2. Сообщает, истёк ли дедлайн или сколько дней осталось.
3. Проверяет корректность формата ввода даты.
"""

from datetime import datetime


# Функция для получения текущей даты
def get_current_date():
    return datetime.now().date()


# Функция для ввода и проверки даты дедлайна
def get_deadline_date():
    formats = ["%d-%m-%Y", "%Y-%m-%d", "%d.%m.%Y", "%Y.%m.%d", "%d/%m/%Y", "%Y/%m/%d"]  # Поддерживаемые форматы
    print("Поддерживаемые форматы даты:")
    for date_format in formats:
        print(f" –{date_format.replace('%d', 'день').replace('%m', 'месяц')
              .replace('%Y', 'год')}")
    while True:
        user_date = input("Введите дату дедлайна: ")
        for date_format in formats:
            try:
                return datetime.strptime(user_date, date_format).date()
            except ValueError:
                continue  # Пробуем следующий формат
        print("Неверный формат даты. Попробуйте снова (например, 25-12-2024 или 25/12/2024).")


# Функция для проверки дедлайна
def check_deadline(current_date, deadline_date):
    delta_days = (deadline_date - current_date).days  # Вычисляем разницу в днях

    # Определяем условие для вывода сообщения
    if delta_days > 0:
        return f"До дедлайна осталось {delta_days} дней."
    elif delta_days < 0:
        return f"Внимание! Дедлайн истёк {-delta_days} дней назад."
    else:
        return "Дедлайн сегодня!"


# Основной код программы
current_date = get_current_date()
print(f"Текущая дата: {current_date.strftime('%d-%m-%Y')}")  # Получаем текущую дату

# Получаем дату дедлайна от пользователя
deadline_date = get_deadline_date()

# Проверяем дедлайн
result = check_deadline(current_date, deadline_date)

# Выводим результат
print(result)
