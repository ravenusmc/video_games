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
            #This line of code will get me the information for the genre
            #returned in a series.
            genre = self.__games[[3]]
            #Once I have the series, I need to pull the specific value of the index
            #for the game.
            game_index = genre.index[0]
            #Once I have the game index in the CSV file, I can use it to target
            #the specific value-in this case the genre.
            genre = genre.genre[game_index]
            print()
            print('The genre for', game_title, 'is', genre)
            print()
            input('Press Enter to back to the main menu')
        elif option == 2:
            publisher = self.__games[[4]]
            game_index = publisher.index[0]
            publisher = publisher.publisher[game_index]
            print()
            print('The publisher for', game_title, 'is', publisher)
            print()
            input('Press Enter to back to the main menu')
        elif option == 3:
            release_date = self.__games[[10]]
            game_index = release_date.index[0]
            release_date = release_date.release_date[game_index]
            print()
            print('The release date for', game_title, 'is', release_date)
            print()
            input('Press Enter to back to the main menu')
        elif option == 4:
            global_sales = self.__games[[9]]
            game_index = global_sales.index[0]
            global_sales = global_sales.global_sales[game_index]
            print()
            print('The global_sales for', game_title, ', in millions, is', global_sales)
            print()
            input('Press Enter to back to the main menu')

    #This method will allow the user to look at games for a specific system.
    def specific_system(self):
        print('\033c')
        system = input('Please enter the name of the system: ')
        self.__games = self.__games[self.__games.platform == system ]
        input('Press Enter to back to the main menu')






# data = Data()
# game_title = data.specific_title()
# print(data.show())
# input('enter')
# data.specific_information(game_title)
