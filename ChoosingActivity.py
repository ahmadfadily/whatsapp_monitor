from Open_chat import open_chat
from Status_check import status_check


def choose_activity(driver) :
    argument = input('For Starting a new chat with new number press 1, for a chat with contact press 2: ')
    if argument == '1':
        Chat_Or_Online = input('if you want to check the status of that person press 1, for only a chat with him press 2: ')
        open_chat(driver, Chat_Or_Online)
        #TODO add the option for the user to check the status availablty (status check) for a number
    elif argument =='2':
        open_chat(status_check(driver))



