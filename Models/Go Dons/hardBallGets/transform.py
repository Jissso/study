import pandas as pd
import numpy as np
import os

# Read all data to Multi Level DataFrame
path = r'/Users/alexandertaylor/Documents/study/Models/Go Dons/hardBallGets/afl_player_stats.csv'
data = pd.read_csv(path)
tuples =[tuple(col.split('.')) for col in data.columns]
data.columns = pd.MultiIndex.from_tuples(tuples)

# Working DataFrame to perform all transforms
df = data


# Dimension Table, contains player details
df_players = df['player']['player']
df_players.drop(columns=df_players.columns[[0, 5]], inplace=True)
df_players = df_players.drop_duplicates().reset_index()

