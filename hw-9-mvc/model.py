from os.path import isfile
phonebook = {1: ['Bill', 'Gates', '000', 'Microsoft Owner']}
NAME, LAST_NAME, PHONE, TITLE  = 0, 1, 2, 3

def add_contact(contact: tuple) -> int:
    new_id = 1 if phonebook == {} else max(phonebook) + 1
    phonebook[new_id] = list(contact)
    return new_id

def find_contact(search_str: str) -> list:
    search_str = input('')
    list_id = []
    for c_id, contact in phonebook.items():
        if search_str.lower() in (str(c_id) + ' ' + ' '.join(contact)).lower():
            list_id.append(c_id)

def change_contact(contact_id: int, new_contact) -> bool:
    if phonebook.get(contact_id):
        phonebook[contact_id] = new_contact
        return True
    else:
        return False

def remove_contact(remove_id: int) -> list:
    if phonebook.get(remove_id):
        return phonebook.pop(remove_id)[1]
    return []

def pb_open(pb_file_name:str) -> bool:
    if isfile(pb_file_name):
        with open(pb_file_name, 'r', encoding='utf-8') as pb_file:
            phonebook.clear()
            for line in pb_file:
                line_list = line.strip().split(';')
                phonebook[line_list[0]] = line_list[1:]
            return True
    return False

def pb_save(pb_file_name: str) -> bool:
    try:
        pb_file = open(pb_file_name, 'w', encoding='utf-8')
        for c_id, contact in phonebook.items():
            pb_file.write(str(c_id)+';'+';'.join(contact)+'\n')
        pb_file.close()
        return True
    except:
        return False

