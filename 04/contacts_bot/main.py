from constants import MENU, MESSAGES, ERROR_MESSAGES
from exceptions import InvalidCommand, NoContactFound, ContactAlreadyExists
from colorama import Fore


def parse_input(user_input: str):
    splitted_input = user_input.split()
    if not len(splitted_input):
        raise InvalidCommand(ERROR_MESSAGES["no_command"])
    cmd, *args = splitted_input
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        raise InvalidCommand(ERROR_MESSAGES["invalid_add_command"])

    name, phone = args
    if name in contacts:
        raise ContactAlreadyExists(ERROR_MESSAGES["contact_already_exists"])

    contacts[name] = phone
    return MESSAGES["contact_added"]


def change_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        raise InvalidCommand(ERROR_MESSAGES["invalid_change_command"])
    
    name, phone = args
    if name not in contacts:
        raise NoContactFound(ERROR_MESSAGES["no_contact"])
    
    contacts[name] = phone
    return MESSAGES["contact_changed"]


def show_phone(args: list, contacts: dict) -> str:
    if len(args) != 1:
        raise InvalidCommand(ERROR_MESSAGES["invalid_show_command"])

    name = args[0]
    if name not in contacts:
        raise NoContactFound(ERROR_MESSAGES["no_contact"])

    return f"{Fore.GREEN}{contacts[name]}"


def show_all(contacts: dict) -> str:
    if not len(contacts):
        return MESSAGES["contacts_empty"]
    all_contacts = ""
    for name, phone in contacts.items():
        all_contacts = all_contacts + f"{Fore.GREEN} {name} - {phone}\n"

    return all_contacts


def main():
    contacts = {}
    print(MESSAGES["welcome"])
    print(MENU)
    while True:
        try:
            user_input = input(MESSAGES["enter_command"])
            command, *args = parse_input(user_input)

            if command in ["close", "exit"]:
                print(MESSAGES["bye"])
                break

            match command:
                case "hello":
                    print(MESSAGES["help_question"])
                case "add":
                    print(add_contact(args, contacts))
                case "change":
                    print(change_contact(args, contacts))
                case "phone":
                    print(show_phone(args, contacts))
                case "all":
                    print(show_all(contacts))
                case _:
                    raise InvalidCommand(ERROR_MESSAGES["invalid_command"])

        except InvalidCommand as e:
            print(e)
            continue
        except NoContactFound as e:
            print(e)
            continue
        except ContactAlreadyExists as e:
            print(e)
            continue


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
