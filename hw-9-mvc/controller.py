import text
import view
import model

def start():
    view.print_menu()
    while True:
        match view.prompt():
            case 'open':
                filename = view.input_file_name()
                if model.pb_open(filename):
                    view.print_message(text.dict_opened_msg)
                else:
                    view.print_error(text.file_not_found)

            case 'save':
                filename = view.input_file_name()
                if model.pb_save(filename):
                    view.print_message(text.dict_saved_msg)
                else:
                    view.print_error(text.anything_wrong_txt)
                    
            case 'print':
                view.show_contacts(model.phonebook)

            case 'append':
                contact = view.input_new_contact()
                c_id = model.add_contact(contact)
                view.print_message(text.contact_added_msg)
                view.print_contact(c_id, model.phonebook)

            case 'remove':
                c_id = view.input_contact_id(text.inp_remove_contact_id)
                model.remove_contact(c_id)
                view.print_message(text.contact_removed_msg)

            case 'change':
                c_id = view.input_contact_id(text.inp_change_contact_id)
                changed_contact = view.input_contact_changes(c_id, model.phonebook)
                if model.change_contact(c_id, changed_contact):
                    view.print_message(text.contact_changed_msg)
                    view.print_contact(c_id, model.phonebook)
                else:
                    view.print_error(text.anything_wrong_txt)

            case 'find':
                search_str = view.input_search_str(text.wh)
                id_list = model.find_contact(search_str)
                for c_id in id_list:
                    view.print_contact(c_id, model.phonebook)

            case 'exit':
                break

            case 'menu':
                view.print_menu()

            case 'error':
                view.print_error(text.anything_wrong_txt)

