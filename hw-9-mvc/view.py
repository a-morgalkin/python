import text
menu_commands = ('open','save', 'print', 'append', 'find', 'change', 'remove', 'exit')

class MenuItem:
    def __init__(self, id, name, command) -> None:
        self.id = id
        self.name = name
        self.command = command
        self.next = None

class Menu:
    def __init__(self, title, prompt = text.prompt_msg) -> None:
        self.title_txt = title
        self.prompt_txt = prompt
        self.head = None

    def additem(self, new_item: MenuItem) -> None:
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_item
        else:
            self.head = new_item

    def show_menu(self) -> None:
        print('\n' + self.title_txt)
        print('-'*25)
        if self.head:
            current = self.head
            while True:
                print(current.name)
                if not current.next:
                    break
                current = current.next

    def whattodo(self) -> str:
        item_id = input(self.prompt_txt)
        if item_id == '0':
            return 'menu'
        if self.head:
            current = self.head
            while True:
                if current.id == item_id:
                    return current.command
                if not current.next:
                    break
                current = current.next
        return 'error'

main_menu = Menu(text.menu_title_txt)
for i in range(len(text.menu_items)):
    main_menu.additem(MenuItem(text.menu_items[i][0],
                               text.menu_items[i],
                               menu_commands[i]))
    
def print_message(msg: str):
    print('... ' + msg)

def print_error(msg: str):
    print('!!! ' + msg)

def print_menu():
    main_menu.show_menu()

def prompt() -> str:
    return main_menu.whattodo()

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
                        ) or phonebook[contact_id].name
        new_lastname = input(text.input_changed_lastname_txt
                        ) or phonebook[contact_id].last_name
        new_phone = input(text.input_changed_phone_txt
                        ) or phonebook[contact_id].phone
        new_title = input(text.input_changed_title_txt
                        ) or phonebook[contact_id].title
        return (new_name, new_lastname, new_phone, new_title)
    else:
        print_error(text.contact_id_err_msg)



