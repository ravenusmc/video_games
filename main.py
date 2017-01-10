#importing all libraries which will be used.
import pandas as pd
import numpy as np




### Functions that will support the main program below here.

def quit():
    print("\033c")
    print('Sorry you don"t want to use the program')
    print('Maybe next time...Good Bye!')


### Main Program functions here.

def main():
    print("\033c")
    print('--------------------------------------------------------------')
    print('\t\tWelcome to Video Games')
    print('\t\tProvide the user with video game stats!')
    print('--------------------------------------------------------------')
    print()
    print('1. Use Program')
    print('2. Quit')
    choice = input('What is your choice: ')
    if choice == 1:
        start_program()
    elif choice == 2:
        quit()

games = pd.read_csv('games.csv')

main()
