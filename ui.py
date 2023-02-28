import Note


def create_note(number):
    title = check_len_text_input(
        input('Введите название заметки: '), number)
    body = check_len_text_input(
        input('Введите описание заметки: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\n------------------- Заметки ------------------- \n\nВыберите нужную функции:\n\n1. Вывод всех заметок \n2. Добавление заметки\n3. Удаление заметки\n4. Редактирование заметки\n5. Список заметок по дате\n6. Список заметок по id\n7. Выход\n\nВведите номер функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text


def goodbuy():
    print("Вы успешно вышли из программы!")
