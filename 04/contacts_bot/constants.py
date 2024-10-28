from colorama import Fore

MENU = f"""{Fore.RESET}
Commands menu:

#1 -{Fore.LIGHTBLACK_EX} hello {Fore.RESET} Say hello to the Bot
#2 -{Fore.BLUE} add <username> <phone> {Fore.RESET} Add new contact
#3 -{Fore.GREEN} change <username> <phone> {Fore.RESET} Change contact
#4 -{Fore.YELLOW} phone <username> {Fore.RESET} Show phone of the contact
#5 -{Fore.WHITE} all {Fore.RESET} Show all contacts
#6 -{Fore.RED} close {Fore.RESET}/{Fore.RED} exit {Fore.RESET} Exit the Bot
"""

ERROR_MESSAGES = {
    "invalid_add_command": f'{Fore.RED}Invalid command!{Fore.RESET} Please enter it in this format "add <username> <phone>"',
    "invalid_change_command": f'{Fore.RED}Invalid command!{Fore.RESET} Please enter it in this format "change <username> <phone>"',
    "invalid_show_command": f'{Fore.RED}Invalid command!{Fore.RESET} Please enter it in this format "phone <username>"',
    "no_command": f"{Fore.RED}Please enter a command.",
    "no_contact": f"{Fore.RED}No name found",
    "contact_already_exists": f"{Fore.RED}This contact already exist.",
    "invalid_command": f"{Fore.RED}Invalid command!",
}

MESSAGES = {
    "welcome": f"{Fore.CYAN}Welcome to the assistant bot!",
    "enter_command": f"{Fore.CYAN}Enter a command: {Fore.RESET}",
    "help_question": f"{Fore.GREEN}How can I help you?",
    "contact_added": f"{Fore.GREEN}Contact added.",
    "contact_changed": f"{Fore.GREEN}Contact changed.",
    "contacts_empty": f"{Fore.GREEN}There are no contacts exists.",
    "bye": f"{Fore.GREEN}Good bye!",
}
