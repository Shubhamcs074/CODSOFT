contacts = [] 

def view_contacts():
    """View all contacts."""
    if not contacts:
        print("You have no contacts to display. Please add contacts first.\n")
        return
    
    print("\nALL Contacts:")
    for index, contact in enumerate(contacts, start=1):
        print(f"\nContact {index}:")
        print(f"Name    : {contact['name']}")
        print(f"Number  : {contact['number']}")
        print(f"Email   : {contact['email']}")
        print(f"Address : {contact['address']}")
    print("\n") 

def add_contact():
    """Add a new contact."""
    name = input("Enter name: ")
    number = input("Enter number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    
   
    contact = {
        "name": name,
        "number": number,
        "email": email,
        "address": address
    }
    
    contacts.append(contact) 
    print("Contact added successfully!\n")


def search_contact():
    """Search for a contact by name or number."""
    search_term = input("Enter name or number to search: ").lower()
    
    found_contacts = [
        contact for contact in contacts
        if search_term in contact['name'].lower() or search_term in contact['number']
    ]
    
    if found_contacts:
        print("\nSearch Results:")
        for contact in found_contacts:
            print(f"\nName    : {contact['name']}")
            print(f"Number  : {contact['number']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}")
    else:
        print(f"No contacts found matching '{search_term}'.\n")

def delete_contact():
    """Delete a contact by name."""
    name_to_delete = input("Enter the name of the contact to delete: ").lower()

    for contact in contacts:
        if contact['name'].lower() == name_to_delete:
            contacts.remove(contact)
            print(f"Contact for '{name_to_delete}' deleted successfully!\n")
            return

    print(f"No contact found with the name '{name_to_delete}'.\n")


def update_contact():
    
    name_to_update = input("Enter the name of the contact to update: ").lower()

    for contact in contacts:
        if contact['name'].lower() == name_to_update:
            print("\nContact found. Enter new details:")
            new_name = input("Enter new name (press Enter to keep current): ") or contact['name']
            new_number = input("Enter new number (press Enter to keep current): ") or contact['number']
            new_email = input("Enter new email (press Enter to keep current): ") or contact['email']
            new_address = input("Enter new address (press Enter to keep current): ") or contact['address']

            contact['name'] = new_name
            contact['number'] = new_number
            contact['email'] = new_email
            contact['address'] = new_address
            print("Contact updated successfully!\n")
            return

    print(f"No contact found with the name '{name_to_update}'.\n")


def contacts_menu():
    """Display the contact management menu."""
    while True:
        print("\n>>>>>> Contact Book <<<<<<")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option (1-6).\n")


contacts_menu()


