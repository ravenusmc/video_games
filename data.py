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
        #title_name = input('Please enter the name of the title: ')
        #self.__games = self.__games[self.__games.name == title_name ]
        self.__games = self.__games[self.__games.name == 'Mario Kart Wii']
        #print("You selected to look at:", title_name)

    def specific_information(self):
        print('\033c')
        print('1. Genre')
        print('2. Publisher')
        print('3. Release Date')
        print('4. Global Sales')
        option = int(input('What is your option? '))
        if option == 1:
            genre = self.__games[[3,4]]
            test = genre[[0]]
            genre = test.genre[1]
            #print(test.genre[1])
            #print('The genre is', genre.iat[1])
            print('The genre is', genre)




data = Data()
data.specific_title()
data.specific_information()
