from os.path import isfile

class Contact:
    def __init__(self, name, last_name, phone, title) -> None:
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.title = title
    def __iter__(self):
        yield self.name
        yield self.last_name
        yield self.phone 
        yield self.title

class PhoneBook:
    def __init__(self) -> None:
        self.phonebook = {1: Contact('Bill', 'Gates', '000', 'Microsoft Owner')}

    def add_contact(self, contact: Contact, contact_id: int = 0) -> int:
        if not contact_id:
            contact_id = 1 if self.phonebook == {} else max(self.phonebook) + 1
        self.phonebook[contact_id] = contact
        return contact_id
    
    def remove_contact(self, remove_id: int) -> None:
        if self.phonebook.get(remove_id):
            self.phonebook.pop(remove_id)
    
    def change_contact(self, contact_id: int, new_contact:Contact) -> bool:
        if self.phonebook.get(contact_id):
            self.add_contact(new_contact, contact_id)
            return True
        else:
            return False
        
    def find_contact(self, search_str: str) -> list:
        list_id = []
        for c_id, contact in self.phonebook.items():
            if search_str.lower() in (str(c_id) + ' ' + ' '.join(contact)).lower():
                list_id.append(c_id)
        return list_id
        
    def pb_open(self, pb_file_name:str) -> bool:
        if isfile(pb_file_name):
            with open(pb_file_name, 'r', encoding='utf-8') as pb_file:
                self.phonebook.clear()
                for line in pb_file:
                    line_list = line.strip().split(';')
                    self.add_contact(Contact(*line_list[1:]), int(line_list[0]))
                return True
        return False
    
    def pb_save(self, pb_file_name: str) -> bool:
        try:
            pb_file = open(pb_file_name, 'w', encoding='utf-8')
            for c_id, contact in self.phonebook.items():
                pb_file.write(str(c_id)+';'+';'.join(contact)+'\n')
            pb_file.close()
            return True
        except:
            return False
