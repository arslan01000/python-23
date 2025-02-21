from datetime import datetime

line = "- " * 11

contacts = [
    {"name": "John", "phone": "123456"},
    {"name": "Jane", "phone": "654321"},
    {"name": "Bob", "phone": "+1234"},
]

while True:
    print("\nCommands: list, find, add, edit, delete, exit")
    command = input("Enter command: \n>> ").strip().lower()

    if command == "list":
        print("\nName       Phone")
        print(line)
        for contact in contacts:
            print(f"{contact['name']:<10} {contact['phone']}")
        print(line)

    elif command == "find":
        name = input("Enter name to search: ").strip()
        found = False
        for contact in contacts:
            if contact["name"].lower() == name.lower():
                print(f"Found: {contact['name']} - {contact['phone']}")
                found = True
                break
        if not found:
            print("Contact not found.")

    elif command == "add":
        name = input("Enter name: ").strip().capitalize()
        phone = input("Enter phone: ").strip()

        exists = any(contact["name"].lower() == name.lower() for contact in contacts)
        if exists:
            print("Contact already exists. Not added.")
        else:
            contacts.append({"name": name, "phone": phone})
            print(line)
            print("Contact added successfully.")

    elif command == "edit":
        name = input("Enter name to edit: ").strip()
        for contact in contacts:
            if contact["name"].lower() == name.lower():
                new_name = input("Enter new name: ").strip()
                new_phone = input("Enter new phone: ").strip()
                contact["name"] = new_name
                contact["phone"] = new_phone
                print(line)
                print("Contact updated successfully.")
                break
        else:
            print("Contact not found.")

    elif command == "delete":
        name = input("Enter name to delete: ").strip()
        for contact in contacts:
            if contact["name"].lower() == name.lower():
                confirm = input(f"Are you sure you want to delete {name}? ").strip().lower()
                if confirm in ("yes", "y", "ok", "да"):
                    contacts.remove(contact)
                    print("Contact deleted successfully.")
                else:
                    print("Deletion cancelled.")
                break
        else:
            print("Contact not found.")

    elif command == "exit":
        print(line)
        print("Exiting ...")
        break

    else:
        print(line)
        print("Unknown command. Please try again.")
