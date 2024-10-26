import re

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a valid user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command."

    return inner

contacts = {}

@input_error
def add_contact(args):
    name, phone = args.split()
    contacts[name] = phone
    return "Contact added."

@input_error
def get_phone(args):
    name = args.strip()
    return f"{name}: {contacts[name]}"

@input_error
def show_all(args=None):
    if not contacts:
        return "No contacts available."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    while True:
        command = input("Enter a command: ").strip().lower()
        
        if command == "add":
            args = input("Enter the name and phone number: ")
            print(add_contact(args))
        
        elif command == "phone":
            args = input("Enter the name to get the phone number: ")
            print(get_phone(args))
        
        elif command == "all":
            print(show_all())
        
        elif command in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        else:
            print("Unknown command. Try again.")

if __name__ == "__main__":
    main()