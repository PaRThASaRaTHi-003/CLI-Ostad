#main file to run

from CLI_manager import add_contact, view_contacts, search_contact, delete_contact

def menu():
    print("\n========= Contact Book Menu ==========")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        search_contact()
    elif choice == '5':
        print("Thank you for using this system!")
    else:
        print("Invalid option. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    menu()

