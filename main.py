#importing all libraries which will be used.
import pandas as pd
import numpy as np

#importing all files that will be used in this program.
from valid import *
from data import *


### Functions that will support the main program below here.

def quit():
    print("\033c")
    print('Sorry you don"t want to use the program')
    print('Maybe next time...Good Bye!')
    print()


### Main Program functions here.

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
    choice = int(input('What is your choice: '))
    print(choice)
    while not main_valid(choice):
        print("That choice is not acceptable!")
        choice = int(input('What is your choice: '))
    if choice == 1:
        start_program()
    elif choice == 2:
        quit()

def start_program():
    print("\033c")
    data = Data()
    print(data.games.head())


#games = pd.read_csv('games.csv')

main()
