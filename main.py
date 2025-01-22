import sys
from sms_polling import poll_sms_messages
from registration_mgnt import register_new_user
from sending_msg_user import sending_msg_user
from json_storage import JSONStorage

storage = JSONStorage("holiday_survivors_json.json")


def introduction_display():
    print("-----------Welcome to the Holiday Survivors!-----------")
    print("-----------------Team HolidaySurvivors-----------------")
    print("-------------------------------------------------------")


def menu_display():
    menu_content = """
            1. Register new user
            2. Sending a custom message to user
            3. Get message
            4. Quit program
            
    """
    print(menu_content)


def menu_dispatch():
    # create a menu dict
    menu_option = {
        "1": command_register_new_user,
        # "2": command_unregister_user,
        "2": command_sending_custom_msg_to_user,
        "3": command_get_msg,
        "4": command_quit_program

    }

    # print menu content
    menu_display()

    # handling user input
    while True:
        try:
            user_input = int(input(f"Please enter a number (1-{len(menu_option)}) to choose an option below:"))
            if user_input < 1 or user_input > len(menu_option):
                raise ValueError(
                    f"Please only enter a number between 1-{len(menu_option)} (1 and {len(menu_option)} included)")
        except ValueError as e:
            print(
                f"Please only enter a number between 1 and {len(menu_option)} (1 and {len(menu_option)} included):" + str(
                    e))
        else:
            break
    # invoke the chosen function
    menu_option[f"{user_input}"]()


def command_get_msg():
    poll_sms_messages(storage)


def command_register_new_user():
    print("-----------Register a new user!-----------")
    print("------------------------------------------")
    user_input = input("Please enter the phone number (enter prefix number following phone number):")
    register_new_user(user_input)
    print("------------------------------------------")


"""
def command_unregister_user():
    print("-----------Unregister a new user!-----------")
    print("--------------------------------------------")
    user_input = input("Please enter the phone number to unregister (enter prefix number following phone number):")
    unregister_user(user_input)
    print("--------------------------------------------")
"""


def command_sending_custom_msg_to_user():
    print("-----------Sending custom msg to user!-----------")
    print("-------------------------------------------------")
    user_input_number = input("Enter a phone number of the receiver:")
    user_input_msg = input("Enter a message:")
    sending_msg_user(user_input_msg, user_input_number)
    print("-------------------------------------------------")


def command_quit_program():
    print("----------------See you next time!---------------")
    print("-------------------------------------------------")
    sys.exit()


def main():
    introduction_display()
    while True:
        menu_dispatch()


if __name__ == "__main__":
    main()
