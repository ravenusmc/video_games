#importing all libraries which will be used.
import pandas as pd
import numpy as np


class Data():

    def __init__(self):
        self.games = pd.read_csv('games.csv')


data = Data()
print(data.games.head())
