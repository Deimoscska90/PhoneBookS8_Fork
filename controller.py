import view, model

def start():
    view.greetings()
    while True:
        view.menu()
        answer = int(input("Выберите соответствующую цифру в меню: "))
        if answer == 1:
            date = model.data()
            view.show_contacts(date)
        elif answer == 2:
            contact = input("Введите данные контакта: ")
            res = model.add_contact(contact)
            view.result(res)
        elif answer == 3:
            contact = input("Введите данные для поиска: ")
            res = model.find_contact(contact)
            view.show_contacts(res)
        elif answer == 4:
            contact = input("Введите имя или фамилию контакта, которого надо удалить: ")
            res = model.del_contact(contact)
            view.result(res)
        elif answer == 5:
            contact = input('Введите имя или фамилию контакта, чей номер будем менять:  ')
            res = model.change_contact(contact)
            view.result(res)
        elif answer == 6:
            break
        else:
            view.error()