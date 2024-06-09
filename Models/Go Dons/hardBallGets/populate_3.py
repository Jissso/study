import requests
import json
import os
import pandas as pd
import numpy as np

# Function called in loop to retrieve data from end points
def fetch_data(url):
    headers = {
        'Content-Type': 'application/json',
        'X-Media-Mis-Token': '43242eda8c2fdd6d153c6929193fa5f9' # Change this if 400
    }

    # Send a GET request to the URL
    response = requests.get(url, headers=headers)
    
    # Return the response content
    return response

fixed_variable = "014"

data = pd.DataFrame()

# Loop through years
for year in range(2021, 2025):
    year_str = f"{year}"
    print(f"Fetching data for year: {year}")

    # Loop through rounds
    for round in range(1, 30):
        round_str = f"{round:02}"  # Format the round number as a two-digit string
        print(f"  Fetching data for round: {round_str}")
        
        # Loop through matches
        for match in range(1, 10):
            match_str = f"{match:02}"  # Format the round number as a two-digit string
            print(f"    Fetching data for match: {match_str}")

            # Construct the URL
            url = f"https://api.afl.com.au/cfs/afl/playerStats/match/CD_M{year_str}{fixed_variable}{round_str}{match_str}"
            r = fetch_data(url)

            if r.status_code != 200:
                print(f"    No data for match {match_str} of round {round_str} in {year}")
            else:
                try:
                    # Get data
                    home_team_data = r.json().get('homeTeamPlayerStats', [])
                    away_team_data = r.json().get('awayTeamPlayerStats', [])
                    
                    if home_team_data and away_team_data:
                        stats_home = pd.json_normalize(home_team_data)
                        stats_away = pd.json_normalize(away_team_data)
                        
                        df_home = stats_home.apply(pd.Series.explode)
                        df_away = stats_away.apply(pd.Series.explode)

                        df_combined = pd.concat([df_home, df_away], axis=0, ignore_index=True)
                        data = pd.concat([data, df_combined], axis=0, ignore_index=True)
                        data['match_id'] = year+round+match
                    else:
                        print(f"    Incomplete data for match {match_str} of round {round_str} in {year}")
                except (KeyError, NotImplementedError) as e:
                    print(f"    Error processing data for match {match_str} of round {round_str} in {year}: {e}")
                except Exception as e:
                    print(f"    Unexpected error for match {match_str} of round {round_str} in {year}: {e}")

# Save the collected data to a CSV file
data.to_csv('afl_player_stats.csv', index=False)
print("Data collection completed and saved to afl_player_stats.csv")
