import db_manager
import view
from db_manager import PhoneBook
pb1 = PhoneBook('phone_db.txt')

def start():
    while True:
        choice = view.menu()
        match choice:
            case 1:
                pb1.__init__('name')
            case 2:
                pb1.save_file()
            case 3:
                pb = pb1.get()
                view.show_contacts(pb)
                # pb1.get()
            case 4:
                new = view.new_contact_input()
                pb1.add(new)
            case 5:
                pb = pb1.get()
                view.show_contacts(pb)
                ind = view.input_id()
                contact = view.new_contact_input()
                pb1.change_contact(ind, contact)

            case 6:
                find = view.find_contact()
                result = pb1.find(find)
                view.show_contacts(result)
            case 7:
                pb = pb1.get()
                view.show_contacts(pb)
                ind = view.input_id()
                name = pb1.get_name(ind)
                if view.confirm('удалить', name):
                    pb1.delete_contact(ind)
            case 8:
                if pb1.check_changes():
                    if view.confirm_changes():
                        pb1.save_file()
                print('До свидания!')
                break
