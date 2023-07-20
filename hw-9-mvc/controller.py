import text
import view
from model import Contact, PhoneBook

def start():
    pb = PhoneBook()
    view.print_menu()
    while True:
        match view.prompt():
            case 'open':
                filename = view.input_file_name()
                if pb.pb_open(filename):
                    view.print_message(text.dict_opened_msg)
                else:
                    view.print_error(text.file_not_found)

            case 'save':
                filename = view.input_file_name()
                if pb.pb_save(filename):
                    view.print_message(text.dict_saved_msg)
                else:
                    view.print_error(text.anything_wrong_txt)
                    
            case 'print':
                view.show_contacts(pb.phonebook)

            case 'append':
                contact = view.input_new_contact()
                c_id = pb.add_contact(Contact(*contact))
                view.print_message(text.contact_added_msg)
                view.print_contact(c_id, pb.phonebook)

            case 'remove':
                c_id = view.input_contact_id(text.inp_remove_contact_id)
                pb.remove_contact(c_id)
                view.print_message(text.contact_removed_msg)

            case 'change':
                c_id = view.input_contact_id(text.inp_change_contact_id)
                changed_contact = view.input_contact_changes(c_id, pb.phonebook)
                if pb.change_contact(c_id, Contact(*changed_contact)):
                    view.print_message(text.contact_changed_msg)
                    view.print_contact(c_id, pb.phonebook)
                else:
                    view.print_error(text.anything_wrong_txt)

            case 'find':
                search_str = view.input_search_str()
                id_list = pb.find_contact(search_str)
                for c_id in id_list:
                    view.print_contact(c_id, pb.phonebook)

            case 'exit':
                break

            case 'menu':
                view.print_menu()

            case 'error':
                view.print_error(text.anything_wrong_txt)

