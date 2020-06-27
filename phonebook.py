class Contact:
    def __init__(self, first_name, second_name, number, favorite=False, **kwargs):
        self.first_name = first_name
        self.second_name = second_name
        self.number = number
        self.favorite = favorite
        self.others_list = []
        for name, info in kwargs.items():
            self.others_list.append(f"{name}: {info}")

    def __str__(self, *args, **kwargs):
        return \
            f"first name: {self.first_name},\n" \
            f"second name: {self.second_name},\n" \
            f"number: {self.number},\n" \
            f"favorites: {self.favorite},\n" \
            f"others:\n     {self.others_list[0]}" \
            f"\n     {self.others_list[1]}"


class PhoneBook(Contact):
    def __init__(self, book_name, *args):
        self.book_name = book_name
        self.all_contacts = []

    def add(self, contact):
        self.all_contacts.append(contact)

    def show_contacts(self):
        for contacts in self.all_contacts:
            print(contacts)

    def del_contact(self, entered_number):
        for contacts in self.all_contacts:
            if contacts.number == entered_number:
                del(self.all_contacts[self.all_contacts.index(contacts)])

    def look_for_favorites(self):
        for contacts in self.all_contacts:
            if contacts.favorite:
                print(contacts)

    def look_for_contact_by_name_second_name(self, name, sec_name):
        for contacts in self.all_contacts:
            if name == self.first_name and sec_name == self.second_name in self.contacts:
                print(contacts)



testbook = PhoneBook("Created book")
print(testbook.book_name)
jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
bob = Contact('Bob', 'Junior', '+71233467809', telegram='@bobby', email='bob@junior.com')
print(jhon)
testbook.add(bob)
testbook.show_contacts()
testbook.del_contact('+71233467809')
testbook.look_for_favorites()
testbook.look_for_contact_by_name_second_name('Bob', 'Junior')