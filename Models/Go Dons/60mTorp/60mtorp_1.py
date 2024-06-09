import pandas as pd
import numpy as np
import os

# Import .csv file
path = '/Users/alexandertaylor/Documents/study/Go Dons/Data/Fact/'
file = os.listdir(path)[1]

# Read .csv to DataFrames
data = pd.read_csv(path + file, skiprows=3)

##### TRANSFORMATIONS ##### ##### TRANSFORMATIONS ##### ##### TRANSFORMATIONS ##### ##### TRANSFORMATIONS #####

# Drop columns - 'fantasyPoints', superCoachPoints', 'namedPosition'
data.drop(['namedPosition', 'fantasyPoints', 'superCoachPoints'], axis=1, inplace=True)

# Groupby subset DataFrame grouped by team and round
df = data.drop(
        [
            'player',
            'cbas',
            'kickins',
            'tog',
            'ruckContests',
            'kickinsPlayon',
            'year'
        ],
    axis=1
    ).groupby(
        [
            'team',
            'round',
            'opponent'
        ]
).sum().reset_index()

# Add column, score (goals + behinds)
df['score'] = (df['goals'] * 6) + df['behinds']

# Add foreign key columns
df['team_key'] = df['team'] + '_' + df['round'].astype('string')
df['opp_key'] = df['opponent'] + '_' + df['round'].astype('string')

# Function to add column to result of the match (Win or Loss) using apply and lambda
def result(row, df):
    oppScore = df.loc[(df['team_key'] == row['opp_key']), 'score'].values[0]
    if row['score'] < oppScore:
        return 'Loss'
    elif row['score'] > oppScore:
        return 'Win'
    else:
        'Draw'

# Add column 'result' to show outcome of match
df['result'] = df.apply(lambda row: result(row, df), axis=1)


# Function use to add 'points' column to 'df'
def points(df, row):
    oppScore = df.loc[(df['team_key'] == row['opp_key']), 'score'].values[0]
    if oppScore > row['score']:
        return 0
    elif oppScore < row['score']:
        return 4
    else:
        2

# Add 'points' column to 'df'
df['points'] = df.apply(lambda row: points(df, row), axis=1)

def oppScore (df, row):
    opp_score = df.loc[(df['team_key'] == row['opp_key']), 'score'].values[0]
    return opp_score

# Add 'opp_score' column, contains opponents score for a match
df['opp_score'] = df.apply(lambda row: oppScore(df, row), axis=1)

# Create 'df_ladder', season ladder
df_ladder = df[['team', 'score', 'opp_score', 'points']].groupby('team').sum()

# Convert 'points' to in int datatype
df_ladder['points'] = df_ladder['points'].astype('int')

# Add percentage 'percentage' column, contains percentage of 'score' divided by 'opp_score'
df_ladder['percentage'] = df_ladder['score'] / df_ladder['opp_score']
df_ladder['percentage'] = df_ladder['percentage'] * 100
df_ladder['percentage'] = df_ladder['percentage'].round(0)
df_ladder['percentage'] = df_ladder['percentage'].apply(lambda x: f'{x:.0f}%')

# Sort 'df_ladder' by 'points' then ' 'percentage'
df_ladder = df_ladder.sort_values(by=['points', 'percentage'], ascending=[False, False])

# Drop 'score' and 'opp_score' from 'df_ladder'
df_ladder.drop(['score', 'opp_score'], axis=1, inplace=True)

df_ladder