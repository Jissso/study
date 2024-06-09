import pandas as pd
import numpy as np
import os

# Import .csv file
path = '/Users/alexandertaylor/Documents/study/60mtorp/data/fact/'
file = os.listdir(path)[1]

# Read .csv to DataFrames
data = pd.read_csv(path + file, skiprows=3)

##### DEFINE UFNCTIONS ##### ##### DEFINE UFNCTIONS ##### ##### DEFINE UFNCTIONS ##### ##### DEFINE UFNCTIONS #####

# Function used to add column to show result of a match (Win or Loss) Create a new opponent score table and merge
def result(row):
    if row['score'] > row['opp_score']:
        return 'Win'
    elif row['score'] < row['opp_score']:
        return 'Loss'
    else:
        return 'Draw'

# Function to add column to result of the match (Win or Loss) using apply and lambda
def result_2(row, df):
    oppScore = df.loc[(df['team_key'] == row['opp_key']), 'score'].values[0]
    if row['score'] < oppScore:
        return 'Loss'
    elif row['score'] > oppScore:
        return 'Win'
    else:
        'Draw'

def ladderPoints(row, df):
    opp_score = df.loc[(df['team_key'] == df['opp_key']), 'score'].values[0]
    if opp_score > df['score']:
        return 0
    elif opp_score == df['score']:
        2
    else:
        return 4

# Function to add column to show points earned from each match
def ladderPoints(df):
    if df['result'] == 'Win':
        return 4
    elif df['result'] == 'Loss':
        return 0
    else:
        return 2

# Fine to add opponent score to working dataframe 'df'
def oppScore(row, df):
    score = df.loc[(df['key_1'] == row['key_2']), 'score'].values

##### TRANSFORMATIONS ##### ##### TRANSFORMATIONS ##### ##### TRANSFORMATIONS ##### ##### TRANSFORMATIONS #####

# Drop columns - 'fantasyPoints', superCoachPoints', 'namedPosition'
df = data.drop(['namedPosition', 'fantasyPoints', 'superCoachPoints'], axis=1)

# Groupby subset DataFrame grouped by team and round
df = df.drop(['player', 'cbas', 'kickins', 'tog', 'ruckContests', 'kickinsPlayon', 'year'], axis=1).groupby(['team', 'round', 'opponent']).sum().reset_index()

# Add column, score (goals + behinds)
df['score'] = (df['goals'] * 6) + df['behinds']

# New Dataframe of opponent scores, for win loss column
opp_score = df[['team', 'round', 'score']]
opp_score.columns = ['opponent', 'round', 'opp_score']

# Merge 'opp_score' to 'df'
#   df = df.merge(opp_score, how='left', left_on=['opponent', 'round'], right_on=['opponent', 'round'])

# Add foreign key columns
df['team_key'] = df['team'] + '_' + df['round'].astype('string')
df['opp_key'] = df['opponent'] + '_' + df['round'].astype('string')

# Add column 'result' to show outcome of match
df['result_2'] = df.apply(lambda row: result_2(row, df), axis=1)

# Add column to show points gained from a match
df['ladderPoints'] = df.apply(lambda x: ladderPoints(x), axis=1)

df['points'] = df.apply(lambda row: ladderPoints(df, row), axis=1)

df['oppScore'] = df['key_2'].apply(lambda x: oppScore(x, df))

df_ladder = df[['team', ]]
# Add column to create foreign key to link bank to 'df' to add opponent to 'df_sum'
  # df_sum['fk_1'] = df_sum['team'] + '_' + df_sum['round'].astype('string')
  # df_sum['fk_2'] = df_sum['opponent'] + '_' + df_sum['round'].astype('string')


#df.merge(df_opp[['opponent', 'sum_key']], how='left', left_on='sum_key', right_on='sum_key')
df.shape

df.columns
df.columns
df['opp_key']
