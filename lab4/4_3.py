import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'

df = pd.read_csv(url)

df['Date'] = pd.to_datetime(df['Date'], dayfirst='false')
df = df.drop(columns=[df.columns[2], df.columns[3]], axis=1)
value = df.columns[1]

df_by_year = df.groupby(df.Date.dt.year)[[value]].sum()
df_by_year.plot()

plt.show()