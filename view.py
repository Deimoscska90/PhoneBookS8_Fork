def greetings():
    print('Вас приветствует телефонный справочник')


def menu():
    print(
        '1 - Просмотр контактов\n'
        '2 - Добавление контактов\n'
        '3 - Поиск контактов в справочнике\n'
        '4 - Удаление контактов\n'
        '5 - Изменение контактов\n'
        '6 - Выход из справочника'
    )


def show_contacts(date):
    print('ФИО: \n'
          'Номер телефона: '
          )


def find_contact(res):
    print('ФИО: \n'
          'Номер телефона: '
          )


def del_contact(res):
    print('Контакт удален.')


def change_contact(res):
    print('Данные контакта изменены.')


def error():
    print('Вы ввели некорректную цифру.')


if __name__ == '__main__':
    menu()