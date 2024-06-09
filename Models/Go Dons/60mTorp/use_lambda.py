import pandas as pd

# Sample DataFrame
data = {
    'team': ['TeamA', 'TeamB', 'TeamA', 'TeamB'],
    'round': [1, 1, 2, 2],
    'score': [100, 90, 80, 85],
    'opponent': ['TeamB', 'TeamA', 'TeamB', 'TeamA'],
    'key_1': ['TeamA_1', 'TeamB_1', 'TeamA_2', 'TeamB_2'],
    'key_2': ['TeamB_1', 'TeamA_1', 'TeamB_2', 'TeamA_2']
}

df = pd.DataFrame(data)

# Create a DataFrame with opponent's scores
opponent_scores = df[['team', 'round', 'score']].copy()
opponent_scores.columns = ['opponent', 'round', 'opponent_score']

# Merge the original DataFrame with the opponent_scores DataFrame
df_merged = pd.merge(df, opponent_scores, how='left', left_on=['opponent', 'round'], right_on=['opponent', 'round'])

# Determine win/loss based on score comparison
df_merged['result'] = df_merged.apply(lambda row: 'Win' if row['score'] > row['opponent_score'] else 'Loss', axis=1)

print(df_merged)
