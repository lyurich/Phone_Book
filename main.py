from controller import start
from db_manager import PhoneBook


pb = PhoneBook('phone_db.txt')
if __name__ == '__main__':
    start()
# pb.__init__('phone_db.txt')
# pb.save_file()
# pb.get()
# pb.add('new_contact')
# # pb.find('find')
# pb.change_contact(5, 'Матвей')
# pb.delete_contact(7)
# pb.get_name(9)
# pb.check_changes()