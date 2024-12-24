titles = []

while True:
    title = input("Введите заголовок (или нажмите Enter для завершения): ")
    if not title:  # Пустой ввод завершает цикл
        break

    clean_title = " ".join(title.split())  # Убираем лишние пробелы

    if not clean_title:  # Проверяем, что заголовок не пустой после очистки
        print("Нельзя добавить пустой заголовок. Попробуйте снова.")
        continue

    if len(clean_title) > 50:  # Проверяем длину заголовка
        print("Заголовок слишком длинный. Попробуйте снова.")
        continue

    # Проверяем уникальность заголовка (без учета регистра)
    if any(clean_title.lower() == existing_title.lower() for existing_title in titles):
        print("Такой заголовок уже существует. Попробуйте другой.")
        continue

    else:
        titles.append(clean_title)  # Добавляем уникальный и непустой заголовок

# Выводим все введенные заголовки
print("\nВаши заголовки:")
for i, t in enumerate(titles, start=1):
    print(f"– Заголовок {i}: {t}")
