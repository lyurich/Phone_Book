from copy import deepcopy

class PhoneBook:
    # phone_book = []
    new_phone_book = []
    path = 'phone_db.txt'
    phone_book = []

    def __init__(self, path):
        self.path = path
        # global phone_book
        # global new_phone_book
        # global path
        with open(path, 'r', encoding='UTF-8') as file:
            data = file.readlines()
            for contact in data:
                new = contact.strip().split(';')
                new_contact = {}
                new_contact['name'] = new[0]
                new_contact['phone'] = new[1]
                new_contact['comment'] = new[2]
                self.phone_book.append(new_contact)
        # new_phone_book = deepcopy(self.phone_book)

    def save_file(self):
        # global phone_book
        # global path
        data = []
        for contact in self.phone_book:
            data.append(';'.join(contact.values()))
        data = '\n'.join(data)
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(data)

    def get(self):
        # global phone_book
        return self.phone_book

    def add(self, new_contact: dict):
        # global phone_book
        self.phone_book.append(new_contact)

    def find(self, find_option: str):
        # global phone_book
        all_find = []
        for contact in self.phone_book:
            for element in contact.values():
                if find_option.lower() in element.lower():
                    all_find.append(contact)
        return all_find

    def change_contact(self, ind: int, contact: dict):
        # global phone_book
        self.phone_book.pop(ind-1)
        self.phone_book.insert(ind-1, contact)

    def delete_contact(self, ind: int):
        # global phone_book
        self.phone_book.pop(ind -1)

    def get_name(self, ind: int):
        # global phone_book
        return self.phone_book[ind-1].get('name')

    def check_changes(self):
        # global phone_book
        # global new_phone_book
        if self.phone_book != self.new_phone_book:
            return True
        else:
            return False