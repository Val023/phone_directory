from logger import input_data, print_data, edit_data, select_and_delete_data


def interface():
    print("Добрый день! Вы попали на специальный бот-справочник от GB! \n 1 - Запись данных \n 2 - Вывод данных \n 3 - Изменить данные \n 4 - Удалить данные")
    command = int(input('Введите число '))

    while command < 1 or command > 4:
        print("Неправильный ввод")
        command = int(input('Введите число '))
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        edit_data()
    elif command == 4:
        select_and_delete_data()
