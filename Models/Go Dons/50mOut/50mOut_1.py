# 60mTorp - Applied Analytics to AFL statistics =]
#   Data Scraped from https://www.wheeloratings.com/afl_match_stats.html?ID={id-num}
#   Scrapes a .json file

# Import Python modules
import requests
import json
import pandas as pd
import numpy as np

# Set url variables to send GET requests to webpages with data
year = 2024
round = 11
id_num = f'{year}{round}'

# Get response usingGET reguest (sourced using PostMan)
url = f'https://www.wheeloratings.com/src/match_stats/table_data/{id_num}.json'
headers = {
  'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
  'Referer': f'https://www.wheeloratings.com/afl_match_stats.html?ID={id_num}',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
  'sec-ch-ua-platform': '"macOS"'
}
response = requests.get(url)#, headers=headers)

# Convert response to normalised JSON format
response_json = response.json()

# Normalise json data
fact_player_stats = pd.json_normalize(response_json['Data'])
fact_team_stats = pd.json_normalize(response_json['TeamData'])

# Read normalised data to DataFrames with pd.Series.explode
df_t = fact_team_stats.apply(pd.Series.explode)
df_p = fact_player_stats.apply(pd.Series.explode)

# View structure of data in 'jfile'
list(fact_player_stats.items())

