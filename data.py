#importing all libraries which will be used.
import pandas as pd
import numpy as np

#importing validation file
from valid import *

#This class sets up the data frame and contains all the methods to act
#on that data frame.
class Data():

    #I have made the games attribute private to protect the information.
    def __init__(self):
        self.__games = pd.read_csv('games.csv')

    #This method will allow me to see all of the information that is contained
    #in games.
    def show(self):
        return self.__games

    #This method will allow the user to select a specific title to look at
    def specific_title(self):
        print('\033c')
        title_name = input('Please enter the name of the title: ')
        self.__games = self.__games[self.__games.name == title_name ]
        print("You selected to look at:", title_name)
        input('Press enter to continue ')
        return title_name

    #This method will allow the user to look at specific information on a game
    #the the user selects.
    def specific_information(self, game_title):
        print('\033c')
        print('1. Genre')
        print('2. Publisher')
        print('3. Release Date')
        print('4. Global Sales')
        option = int(input('What is your option? '))
        while not specific_information_valid(option):
            print('That is not a valid option!')
            option = int(input('What is your option? '))
        if option == 1:

            genre = self.__games[[3]]
            print(genre)
            input('Enter test 1 ')

            genre = genre.genre[genre]
            # genre = genre.genre[1] works!
            print(genre)
            input('enter test 2 ')

            print('The genre for', game_title, 'is', genre)
            print()
            input('Press Enter to back to the main menu')
        elif option == 2:
            publisher = self.__games[[4]]
            publisher_name = publisher[[0]]
            publisher = publisher_name.publisher[1]
            print('The publisher for', game_title, 'is', publisher)
            print()
            input('Press Enter to back to the main menu')
        elif option == 3:
            release_date = self.__games[[10]]
            release_data_name = release_date[[0]]
            release_date = release_data_name.release_date[1]
            print('The release date for', game_title, 'is', release_date)
            print()
            input('Press Enter to back to the main menu')
        elif option == 4:
            global_sales = self.__games[[9]]
            global_sales = global_sales.global_sales[1]
            print('The global_sales for', game_title, ', in millions, is', global_sales)
            print()
            input('Press Enter to back to the main menu')




data = Data()
game_title = data.specific_title()
# print(data.show())
# input('enter')
data.specific_information(game_title)
