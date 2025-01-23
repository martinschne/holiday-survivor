import sys

from json_storage import JSONStorage
from registration import register_new_user
from sms_sender import sending_msg_user
from sms_polling import poll_sms_messages

storage = JSONStorage("holiday_survivors_json.json")


def introduction_display():
    """
    Displays the introduction of the program, including the name of the application and the team name.

    :returns: None
    """
    print("-----------Welcome to the Holiday Survivors!-----------")
    print("-----------------Team HolidaySurvivors-----------------")
    print("-------------------------------------------------------")


def menu_display():
    """
    Displays the menu of the program, including the options to register a new user, to send a custom message to user, to get message, and to quit the program.

    :returns: None
    """
    menu_content = """
            1. Register new user
            2. Sending a custom message to user
            3. Get message
            4. Quit program
            
    """
    print(menu_content)


def menu_dispatch():
    # create a menu dict
    """
    Displays the menu of the program, including the options to register a new user, to send a custom message to user, to get message, and to quit the program.

    The function takes no arguments, and it will keep asking the user for input until it receives a valid number between 1 and the length of the menu options.

    :raises ValueError: If the user enters a number that is not between 1 and the length of the menu options.
    :returns: None
    """
    menu_option = {
        "1": command_register_new_user,
        # "2": command_unregister_user, # currently not in use
        "2": command_sending_custom_msg_to_user,
        "3": command_get_msg,
        "4": command_quit_program,
    }

    # print menu content
    menu_display()

    # handling user input
    while True:
        try:
            user_input = int(
                input(
                    f"Please enter a number (1-{len(menu_option)}) to choose an option below:"
                )
            )
            if user_input < 1 or user_input > len(menu_option):
                raise ValueError(
                    f"Please only enter a number between 1-{len(menu_option)} (1 and {len(menu_option)} included)"
                )
        except ValueError as e:
            print(
                f"Please only enter a number between 1 and {len(menu_option)} (1 and {len(menu_option)} included):"
                + str(e)
            )
        else:
            break
    # invoke the chosen function
    menu_option[f"{user_input}"]()


def command_get_msg():
    poll_sms_messages(storage)


def command_register_new_user():
    """
    Prompts user to input a phone number and registers the number to the service.
    """
    print("-----------Register a new user!-----------")
    print("------------------------------------------")
    user_input = input(
        "Please enter the phone number (enter prefix number following phone number):"
    )
    register_new_user(user_input)
    print("------------------------------------------")


# currently not in use
# def command_unregister_user():
#     print("-----------Unregister a new user!-----------")
#     print("--------------------------------------------")
#     user_input = input("Please enter the phone number to unregister (enter prefix number following phone number):")
#     unregister_user(user_input)
#     print("--------------------------------------------")



def command_sending_custom_msg_to_user():
    """
    Prompts user to input a phone number and a message, and sends the message to the user.
    """
    print("-----------Sending custom msg to user!-----------")
    print("-------------------------------------------------")
    user_input_number = input("Enter a phone number of the receiver:")
    user_input_msg = input("Enter a message:")
    sending_msg_user(user_input_msg, user_input_number)
    print("-------------------------------------------------")


def command_quit_program():
    """
    Prints a goodbye message and exits the program.

    This function is invoked by the menu option 4, "Quit program".
    """
    print("----------------See you next time!---------------")
    print("-------------------------------------------------")
    sys.exit()


def main():
    """
    The main entry point of the program.

    This function first displays an introduction, and then enters an infinite loop,
    where it displays the menu and invokes the chosen function until the user chooses
    to quit the program.
    """
    introduction_display()
    while True:
        menu_dispatch()


if __name__ == "__main__":
    main()
