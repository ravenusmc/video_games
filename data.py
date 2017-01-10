#importing all libraries which will be used.
import pandas as pd
import numpy as np


class Data():

    #I have made the games attribute private to protect the information. 
    def __init__(self):
        self.__games = pd.read_csv('games.csv')

    def show(self):
        return self.__games


# data = Data(games)
# print(data.games.head())
