import json
import os
import datetime

# Функция для загрузки заметок из файла json
def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as f:
            notes = json.load(f)
    else:
        notes = {}
    return notes

# Функция для сохранения заметок в файл json
def save_notes(notes):
    with open("notes.json", "w") as f:
        json.dump(notes, f)

# Функция для вывода списка заметок на экран
def print_notes(notes):
    print("Список заметок:")
    for note in notes.values():
        print(f"{note['id']}: {note['title']} \nДата создания: {note['created_at']} \nДата изменения: {note['updated_at']}")

# Функция для вывода информации о заметке на экран
def print_note_info(note):
    print(f"Идентификатор: {note['id']}")
    print(f"Заголовок: {note['title']}")
    print(f"Дата создания: {note['created_at']}")
    print(f"Дата изменения: {note['updated_at']}")
    print(f"Тело заметки: {note['body']}")

# Функция для добавления новой заметки
def add_note():
    notes = load_notes()
    # Генерируем уникальный идентификатор для новой заметки
    new_id = str(len(notes) + 1)
    # Получаем от пользователя заголовок и тело заметки
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    # Создаем новую заметку
    new_note = {
        "id": new_id,
        "title": title,
        "body": body,
        "created_at": str(datetime.datetime.now()),
        "updated_at": str(datetime.datetime.now()),
    }
    # Добавляем новую заметку в словарь всех заметок
    notes[new_id] = new_note
    # Сохраняем изменения в файл
    save_notes(notes)
    print(f"Заметка с идентификатором {new_id} успешно добавлена.")

# Функция для редактирования заметки
def edit_note():
    notes = load_notes()
    # Получаем от пользователя идентификатор заметки, которую нужно редактировать
    note_id = input("Введите идентификатор заметки, которую нужно редактировать: ")
    # Проверяем, существует ли заметка с таким идентификатором
    if note_id in notes:
        # Получаем от пользователя новый заголовок и тело заметки
        new_title = input("Введите новый заголовок заметки: ")
        new_body = input("Введите новый текст заметки: ")
        # Обновляем заголовок, тело заметки и дату/время изменения
        notes[note_id]["title"] = new_title
        notes[note_id]["body"] = new_body
        notes[note_id]["updated_at"] = str(datetime.datetime.now())
        # Сохраняем изменения в файл
        save_notes(notes)
        print(f"Заметка с идентификатором {note_id} успешно изменена.")
    else:
        print(f"Заметка с идентификатором {note_id} не найдена.")

# Функция для удаления заметки
def delete_note():
    notes = load_notes()
    # Получаем от пользователя идентификатор заметки, которую нужно удалить
    note_id = input("Введите идентификатор заметки, которую нужно удалить: ")
    # Проверяем, существует ли заметка с таким идентификатором
    if note_id in notes:
        # Удаляем заметку из словаря всех заметок
        del notes[note_id]
        # Обновляем идентификаторы оставшихся заметок, чтобы они шли без пропусков
        for i, note in enumerate(notes.values()):
            note["id"] = str(i + 1)
        # Сохраняем изменения в файл
        save_notes(notes)
        print(f"Заметка с идентификатором {note_id} успешно удалена.")
    else:
        print(f"Заметка с идентификатором {note_id} не найдена.")

# Функция для выборки заметок по дате
def filter_notes_by_date():
    notes = load_notes()
    # Получаем от пользователя дату, по которой нужно выбрать заметки
    date_str = input("Введите дату в формате ГГГГ-ММ-ДД: ")
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Неправильный формат даты.")
        return
    # Ищем заметки, созданные или измененные в указанную дату
    filtered_notes = []
    for note in notes.values():
        created_at = datetime.datetime.fromisoformat(note["created_at"])
        updated_at = datetime.datetime.fromisoformat(note["updated_at"])
        if created_at.date() == date.date() or updated_at.date() == date.date():
            filtered_notes.append(note)
    # Выводим найденные заметки на экран
    if filtered_notes:
        print(f"Список заметок за {date_str}:")
        for note in filtered_notes:
            print(f"{note['id']}: {note['title']} \nДата создания: {note['created_at']} \nДата изменения: {note['updated_at']}")
    else:
        print(f"Заметки за {date_str} не найдены.")

# Функция для выборки заметок по идентификатору
def filter_notes_by_id():
    notes = load_notes()
    # Получаем от пользователя идентификатор заметки, которую нужно выбрать
    note_id = input("Введите идентификатор заметки: ")
    # Проверяем, существует ли заметка с таким идентификатором
    if note_id in notes:
        # Выводим информацию о заметке на экран
        print_note_info(notes[note_id])
    else:
        print(f"Заметка с идентификатором {note_id} не найдена.")

# Функция для вывода справочной информации
def print_help():
    print("Команды:")
    print("add - добавить новую заметку")
    print("edit - редактировать существующую заметку")
    print("delete - удалить существующую заметку")
    print("list - вывести список всех заметок")
    print("filter_date - выбрать заметки по дате")
    print("filter_id - выбрать заметку по идентификатору")
    print("help - вывести эту справку")
    print("exit - выйти из программы")

# Главная функция приложения
def main():
    print("Добро пожаловать в приложение заметки!")
    print_help()
    while True:
        # Читаем команду пользователя
        command = input("Введите команду: ")
        if command == "add":
            add_note()
        elif command == "edit":
            edit_note()
        elif command == "delete":
            delete_note()
        elif command == "list":
            notes = load_notes()
            print_notes(notes)
        elif command == "filter_date":
            filter_notes_by_date()
        elif command == "filter_id":
            filter_notes_by_id()
        elif command == "help":
            print_help()
        elif command == "exit":
            print("До свидания!")
            break
        else:
            print("Неизвестная команда. Введите 'help' для получения справки.")

if __name__ == "__main__":
    main()
