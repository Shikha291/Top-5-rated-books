import pandas as pd

df = pd.read_csv("bestsellers with categories.csv", sep=',')

price = input("Books below price:")

df1 = df[df['Price'] < int(price)]

df1.sort_values(['User Rating'])

print("Top 5 rated books below this price:\n", df1['Name'].head())
