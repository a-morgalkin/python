import text
menu_commands = ('open','save', 'print', 'append', 'find', 'change', 'remove', 'exit')
menu = tuple(zip([item[0] for item in text.menu_items], text.menu_items, menu_commands))
MENU_ID, MENU_TEXT, MENU_COMMAND = 0, 1, 2
NAME, LAST_NAME, PHONE, TITLE  = 0, 1, 2, 3

def print_message(msg: str):
    print('... ' + msg)

def print_error(msg: str):
    print('!!! ' + msg)

def print_menu():
    for item in menu:
        print(item[MENU_TEXT])

def prompt() -> str:
    inp_str = input(text.prompt_msg)
    for item in menu:
        if inp_str == item[MENU_ID]:
            return item[MENU_COMMAND]
    if inp_str == '0':
        return 'menu'
    return 'error'

def print_contact(contact_id, phonebook):
    print(contact_id, *phonebook[contact_id], sep='\t')

def show_contacts(phonebook):
    print('-'*50)
    for c_id in phonebook:
        print_contact(c_id, phonebook)
    print('-'*50)

def input_file_name() -> str:
    return input(text.inp_file_name_txt) or 'phonebook.txt'

def input_new_contact() -> tuple:
    name = input(text.input_name_msg) 
    lastname = input(text.input_last_name_msg)
    phone = input(text.input_phone_msg) 
    title = input(text.input_title_msg) 
    return name, lastname, phone, title

def input_contact_id(msg: str) -> int:
    try:
        c_id = int(input(msg))
    except:
        c_id = -1
    return c_id

def input_search_str() -> str:
    return input(text.what_search_msg)

def input_contact_changes(contact_id, phonebook) -> tuple:
    if phonebook.get(contact_id):
        print_contact(contact_id, phonebook)
        new_name = input(text.input_changed_name_txt
                        ) or phonebook[contact_id][NAME]
        new_lastname = input(text.input_changed_lastname_txt
                        ) or phonebook[contact_id][LAST_NAME]
        new_phone = input(text.input_changed_phone_txt
                        ) or phonebook[contact_id][PHONE]
        new_title = input(text.input_changed_title_txt
                        ) or phonebook[contact_id][TITLE]
        return (new_name, new_lastname, new_phone, new_title)
    else:
        print_error(text.contact_id_err_msg)



