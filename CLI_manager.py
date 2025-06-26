#to manage CLI

from contacts import Contact
from file_manager import new_contact, save_contact, save_contacts_2

contacts = new_contact()

def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter 11 digit Mobile Number: ").strip()
    email = input("Enter a Valid Email Address: ").strip()
    address = input("Enter Address: ").strip()

    if any(c.phone == phone for c in contacts):
        print("A contact with this phone number already exists.")
    
    try:
        contact_info = Contact(name, phone, email, address)
        contacts.append(contact_info)
        save_contact(contact_info)
        print("Contact added successfully!")
    except ValueError as e:
        print("Error: ", e)

def view_contacts():
    if not contacts:
        print("No contacts to display.")
    else:
        for i, c in enumerate(contacts, start = 1):
            print(f'\nContact {i}:\n{c}')

def search_contact():
    term = input("Enter search term (name/phone/email/address): ").lower()
    find = [c for c in contacts if term in c.name.lower() or term in c.email.lower() or term in c.phone or term in c.address.lower()]
    if not find:
        print("No contacts found.")
    else:
        for c in find:
            print("\n" + str(c))

def delete_contact():
    phone = input("Enter the phone number of the contact to delete: ")
    global contacts
    new_contact = [c for c in contacts if c.phone != phone]
    if len(new_contact) == len(contacts):
        print("No contact found with this phone number.")
    else:
        contacts = new_contact
        save_contacts_2(contacts)
        print("Contact deleted successfully!")