from os.path import isfile

menu = (('1', '1. Открыть справочник', 'open'),
        ('2', '2. Сохранить справочкник', 'save'),
        ('3', '3. Показать контакты', 'print'),
        ('4', '4. Добавить контакты', 'append'),
        ('5', '5. Найти контакт', 'find'),
        ('6', '6. Изменить контакт', 'change'),
        ('7', '7. Удалить контакт', 'remove'),
        ('8', '8. Выход', 'exit'))
        #'0' reserved for print menu

# contacts = {id int key, ['name', 'phone', 'title'] }
phonebook = {1: ['Bill', 'Gates', '000', 'Microsoft Owner']}
NAME, LAST_NAME, PHONE, TITLE  = 0, 1, 2, 3
MENU_ID, MENU_TEXT, MENU_COMMAND = 0, 1, 2

def print_menu():
    for item in menu:
        print(item[MENU_TEXT])

def get_command(inp_str):
    for item in menu:
        if inp_str == item[MENU_ID]:
            return item[MENU_COMMAND]
    if inp_str == '0':
        return 'menu'
    return 'error'

def print_contact(contact_id):
    print(contact_id, *phonebook[contact_id], sep='\t')

def show_contacts():
    print('-'*50)
    for c_id in phonebook:
        print_contact(c_id)
    print('-'*50)

def add_contact():
    new_name = input('>>> Введите имя > ') or 'John'
    new_lastname = input('>>> Введите фамилию > ') or 'Doe'
    new_phone = input('>>> Введите телефон > ') or '---'
    new_title = input('>>> Введите должность > ') or 'Umbrella'
    new_id = 1 if phonebook == {} else max(phonebook) + 1
    phonebook[new_id] = (new_name, new_lastname, new_phone, new_title)
    print('...Конакт добавлен:')
    print_contact(new_id)

def find_contact():
    search_str = input('>>> Что ищем? > ')
    for c_id, v in phonebook.items():
        # if search_str == str(c_id) or len(set(fld for fld in v if search_str.lower() in fld.lower())) >0:
        # ^ поиск по ID, всем полям и подстроке независимо от регистра
        if search_str.lower() in (str(c_id) + ' ' + ' '.join(v)).lower():
            print_contact(c_id)

def change_contact():
    try:
        contact_id = int(input('>>> Введите ID контакта для изменения > '))
    except:
        contact_id = -1
    if phonebook.get(contact_id):
        print('...контакт:')
        print_contact(contact_id)
        new_name = input('>>> Введите новое имя (enter оставить)> ') or phonebook[contact_id][NAME]
        new_lastname = input('>>> Введите новую фамилию имя (enter оставить)> ') or phonebook[contact_id][LAST_NAME]
        new_phone = input('>>> Введите новый телефон (enter оставить) > ') or phonebook[contact_id][PHONE]
        new_title = input('>>> Введите новую должность (enter оставить) > ') or phonebook[contact_id][TITLE]
        phonebook[contact_id] = (new_name, new_lastname, new_phone, new_title)
        print('... контакт изменен:')
        print_contact(contact_id)
        print()
    else:
        print('!!! Контакта с таким ID нет в базе. Воспользуйтесь поиском...')

def remove_contact():
    try:
        remove_id = int(input('>>> Введите ID контакта для удаления > '))
    except:
        remove_id = -1
    if phonebook.get(remove_id):
        phonebook.pop(remove_id)
        print('...Контакт удален')

def pb_open():
    pb_file_name = input('>>> Введите имя файла [phonebook.txt] > ') or 'phonebook.txt'
    if isfile(pb_file_name):
        pb_file = open(pb_file_name, 'r', encoding='utf-8')
        phonebook.clear()
        count = 1
        for line in pb_file:
            phonebook[count] = line.strip().split(';')
            count += 1
        pb_file.close()
        print('... Справочник загружен')
    else:
        print('!!! Такого файла не сущетвует')

def pb_save():
    pb_file_name = input('>>> Введите имя файла [phonebook.txt] > ') or 'phonebook.txt'
    pb_file = open(pb_file_name, 'w', encoding='utf-8')
    for contact in phonebook.items():
        pb_file.writelines(';'.join(contact[1])+'\n')
    pb_file.close()
    print('...Справочник сохранен')

print_menu()
while True:
    inp = input('Введите команду, [0 - меню] > ')
    match get_command(inp):
        case 'open':
            pb_open()
        case 'save':
            pb_save()
        case 'print':
            show_contacts()
        case 'append':
            add_contact()
        case 'remove':
            remove_contact()
        case 'change':
            change_contact()
        case 'find':
            find_contact()
        case 'exit':
            break
        case 'menu':
            print_menu()
        case 'error':
            print('!!! Такой команды нет')
        case _:
            print('!!! Неизвестная выход')
