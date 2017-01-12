#This file will contain all of the functions for validation in my program

def main_valid(choice):
    if choice == 1 or choice == 2:
        return True
    else:
        return False

def specific_information_valid(option):
    if option == 1 or option == 2 or option == 3 or option == 4:
        return True
    else:
        return False
