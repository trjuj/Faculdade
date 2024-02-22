import pandas as pd

data = pd.read_csv('Amazon Sale Report.csv', sep=',')

df = pd.read_csv('Amazon Sale Dates 2.csv', sep=',')

# df = data['Date']

# df.sort_values()

# df.to_csv('Amazon Sale Dates 2.csv', index=False)