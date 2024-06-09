# 60mTorp - Applied Analytics to AFL statistics =]
#   Data Scraped from https://www.wheeloratings.com/afl_match_stats.html?ID={id-num}
#   Scrapes a .json file

# Import Python modules
import requests
import json
import pandas as pd
import numpy as np

##### Get data, execute For loop #####

# Assign variables for loops 
# Create lists for seasons and rounds to loop through
seasons = [2012 + i for i in range(13)]
rounds = [f'{x:02}' for x in range(1, 31)]

# Create empty DataFrames to populate data into
team_stats = pd.DataFrame()
player_stats = pd.DataFrame()

# Execute For loops, loop through AFL seasons and rounds
for season in seasons:
  #season = 2024
  for round in rounds:
    #round = '13'
    # Assign number (string) to be using in 'url'
    id_num = f'{season}{round}'

    # Send GET requests to wheeloratings webpage
    url = f'https://www.wheeloratings.com/src/match_stats/table_data/{id_num}.json'
    
    r = requests.get(url)

    # Check IF request response is '404' if yes load data to tables in NO then BREAK and proceed to next 'round'
    if r.status_code == 200:
      
      # Convert response to normalised JSON format
      match_stats = r.json()
      fact_team_stats = pd.json_normalize(match_stats['TeamData'])
      fact_player_stats = pd.json_normalize(match_stats['Data'])

      # Explode data (currently in key pairs) to Dataframe and assign to 'df'
      df_t = fact_team_stats.apply(pd.Series.explode)
      df_p = fact_player_stats.apply(pd.Series.explode)

      # Concat big Dataframes
      team_stats = pd.concat([team_stats, df_t], axis=0, ignore_index=True)
      player_stats = pd.concat([player_stats, df_p], axis=0, ignore_index=True)
    else:
      continue
