class Contact:
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = email
        self.telephone = telephone

    def __str__(self):
        return f"{self.name:<15} {self.email:<20} {self.telephone}"


class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if not self.contacts:
            print("No contacts in the list.")
            return

        print("Contact List:")
        print("-" * 50)
        print(f"Name            Email                Telephone")
        print("-" * 50)
        for contact in self.contacts:
            print(contact)