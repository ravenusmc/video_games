#importing all libraries which will be used.
import pandas as pd
import numpy as np

#importing all files that will be used in this program.
from valid import *
from data import *
from support import *

####### Main Program functions here. #########

#This is the main function of the program that will be used to run it.
def main():
    print("\033c")
    print('--------------------------------------------------------------')
    print('\t\tWelcome to Video Games')
    print('\t\tProvide the user with video game stats!')
    print('--------------------------------------------------------------')
    print()
    print('1. Use Program')
    print('2. Quit')
    #This object will be called to execute all support functions
    support = Support()
    choice = int(input('What is your choice: '))
    print(choice)
    while not main_valid(choice):
        print('That choice is not acceptable!')
        choice = int(input('What is your choice: '))
    if choice == 1:
        start_program(support)
    elif choice == 2:
        support.quit()

#This function will allow the user to select what they want to do in the
#program.
def start_program(support):
    print("\033c")
    #I am creating an object to hold all of the data
    data = Data()
    print('1. Look at information about a specific game')
    print('2. Look at information about a specific system')
    print('3. Quit')
    choice = int(input('What is your choice? '))
    if choice == 1:
        game_title = data.specific_title()
        data.specific_information(game_title)
        start_program(support)
    elif choice == 2:
        data.specific_system()
        print(data.show())
        input('Press Enter to Continue ')
        start_program(support)
    elif choice == 3:
        support.quit()

main()
