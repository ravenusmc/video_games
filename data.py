#importing all libraries which will be used.
import pandas as pd
import numpy as np

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

    def specific_information(self, game_title):
        print('\033c')
        print('1. Genre')
        print('2. Publisher')
        print('3. Release Date')
        print('4. Global Sales')
        option = int(input('What is your option? '))
        if option == 1:
            genre = self.__games[[3]]
            #This center line, in options 1 through 3 I really do not need.
            genre_name = genre[[0]]
            genre = genre_name.genre[1]
            print('The genre for', game_title, 'is', genre)
        elif option == 2:
            publisher = self.__games[[4]]
            publisher_name = publisher[[0]]
            publisher = publisher_name.publisher[1]
            print('The publisher for', game_title, 'is', publisher)
        elif option == 3:
            release_date = self.__games[[10]]
            release_data_name = release_date[[0]]
            release_date = release_data_name.release_date[1]
            print('The release date for', game_title, 'is', release_date)
        elif option == 4:
            global_sales = self.__games[[9]]
            global_sales = global_sales.global_sales[1]
            print('The global_sales for', game_title, ', in millions, is', global_sales)




# data = Data()
# data.specific_title()
# data.specific_information()
