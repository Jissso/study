import pandas as pd
import numpy as np
import time
import datetime
import matplotlib as mlt
import mplfinance as mpf

ticker = 'AUDUSD=X'
period1 = int(time.mktime(datetime.datetime(2010, 7, 16, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2023, 7, 16, 23, 59).timetuple()))
interval = '1d'

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(query_string)

# Sort the DataFrame by date in ascending order
df = df.sort_values('Date')

# Calculate the rolling mean of the last 30 'Close' prices
df['Last_30_Close'] = df['Close'].rolling(200).mean()

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
df
# Set the 'Date' column as the index
df.set_index('Date', inplace=True)

df
#my_style = mpf.make_mpf_style(base_mpf_style='classic', gridstyle=':', y_on_right=True)

# Plot the candlestick chart
#mpf.plot(df, type='candle', title='AUDUSD', ylabel='Close', mav=(200,))

# Show the plot
#mpf.show()