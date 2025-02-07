# Описание файлов

## Файлы этапа 1

### greetings.py (Задание 1): 
- Созданы переменные и реализован и вывод на экран

### date_changer.py (Задание 2): 
- Импортирована библиотека datetime. 
- Создана функция get_valid_date для запроса корректной даты у пользователя.
- Реализовано преобразование формата отображения дат для пользователя.

### add_input.py (Задание 3),
- Создана функция get_titles, которая запрашивает количество заголовков у пользователя.

### add_list.py (Задание 4):
- Создана функция get_titles, которая запрашивает ровно 3 заголовка у пользователя.
- Создан список для хранения заголовков.
- Введенные данные отображаются, включая список заголовков.

### final.py (Задание 5):
- Все данные организованы в словарь для заметки.
- Релизованы функции get_valid_date и get_titles, результаты которых, так же хранятся в словаре
- Все данные выводятся на экран в структурированном виде.

# Описание файлов

## Файлы этапа 2

### add_titles_loop.py
**Функциональность:**
- Запрашивает у пользователя заголовки заметки.
- Позволяет завершить ввод специальной командой или пустым вводом.
- Выводит итоговый список добавленных заголовков.

**Пример работы:**
```
Введите заголовок (или оставьте пустым для завершения): Основные идеи
Введите заголовок (или оставьте пустым для завершения): Список задач
Введите заголовок (или оставьте пустым для завершения):

Заголовки заметки:
- Основные идеи
- Список задач
```

### update_status.py
**Функциональность:**
- Показывает текущий статус заметки.
- Предлагает изменить статус на один из предложенных.
- Обрабатывает некорректный ввод.

**Пример работы:**
```
Текущий статус заметки: "в процессе"
Выберите новый статус заметки:
1. выполнено
2. в процессе
3. отложено
4: Другое (введите свой статус)
Ваш выбор: 1
Статус заметки успешно обновлён на: "выполнено"
```

### check_deadline.py
**Функциональность:**
- Запрашивает дату дедлайна и сравнивает её с текущей датой.
- Сообщает, истёк ли дедлайн или сколько дней осталось.
- Проверяет корректность формата ввода.

**Пример работы:**
```
Текущая дата: 27-12-2024
Введите дату дедлайна (в формате день-месяц-год): 25-12-2024
Внимание! Дедлайн истёк 2 дня назад.
```

### multiple_notes.py
**Функциональность:**
- Создаёт несколько заметок через ввод данных (имя, заголовок, описание, статус, дату создания, дедлайн).
- Хранит заметки в списке словарей.
- Выводит список всех заметок.

**Пример работы:**
```
Меню:
1. Добавить заметку
2. Удалить заметку
3. Показать все заметки
4. Выйти
Выберите нужный пункт (1-4): 1

Добро пожаловать в менеджер заметок! Вы можете добавить новую заметку.
Введите имя пользователя: Алексей
Введите заголовок заметки: Список покупок
Введите описание заметки: Купить продукты на неделю
Введите статус заметки (новая, в процессе, выполнено): новая
Введите дату создания (день-месяц-год): 27-11-2024
Введите дедлайн (день-месяц-год): 30-11-2024

Список заметок:
1. Имя: Алексей
   Заголовок: Список покупок
   Описание: Купить продукты на неделю
   Статус: новая
   Дата создания: 27-11-2024
   Дедлайн: 30-11-2024
```

### delete_note.py
**Функциональность:**
- Удаляет заметку по имени пользователя или заголовку.
- Выводит сообщение, если заметка не найдена.
- Обновляет список заметок.

**Пример работы:**
```
Текущие заметки:
1. Имя: Алексей
   Заголовок: Список покупок
   Описание: Купить продукты на неделю
2. Имя: Мария
   Заголовок: Учеба
   Описание: Подготовиться к экзамену

Введите имя пользователя или заголовок для удаления заметки: Список покупок
Успешно удалено. Остались следующие заметки:
1. Имя: Мария
   Заголовок: Учеба
   Описание: Подготовиться к экзамену
```