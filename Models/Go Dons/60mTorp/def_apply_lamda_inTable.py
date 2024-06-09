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

# Function to determine win/loss
def determine_result(row, df):
    # Get the opponent's score using the opponent's key
    opponent_score = df.loc[(df['key_1'] == row['key_2']), 'score'].values[0]
    # Compare the current row's score with the opponent's score
    return 'Win' if row['score'] > opponent_score else 'Loss'

# Apply the function to each row
df['result'] = df.apply(lambda row: determine_result(row, df), axis=1)

print(df)