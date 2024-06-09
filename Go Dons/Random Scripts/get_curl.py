import pandas as pd

def fetch_season_stats(season):
    stats = []
    for round_number in range(1, 24):  # Assuming 23 rounds in a season
        try:
            round_stats = pyAFL.get_round_stats(season, round_number)
            stats.extend(round_stats)
        except Exception as e:
            print(f"Failed to fetch stats for season {season}, round {round_number}: {e}")
    return stats

# Fetch stats for the 2022, 2023, and 2024 seasons
seasons = [2022, 2023, 2024]
all_stats = []

for season in seasons:
    season_stats = fetch_season_stats(season)
    all_stats.extend(season_stats)

# Convert to DataFrame
df = pd.DataFrame(all_stats)
df.to_csv('afl_player_stats_2022_2024.csv', index=False)

print("Player stats for seasons 2022, 2023, and 2024 have been saved to 'afl_player_stats_2022_2024.csv'")
