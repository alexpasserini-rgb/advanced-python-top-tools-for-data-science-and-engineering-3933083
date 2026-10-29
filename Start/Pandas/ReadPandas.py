# Example file for Advanced Python: Top Tools for Data Science
# Using the Pandas library create and access a DataFrame


import pandas as pd


# 1. Read data from a CSV file and describe the DataFrame
# df=pd.read_csv('sales_data.csv')
# print(df)

# 2. Use only a subset of the columns
# df=pd.read_csv('sales_data.csv', usecols=['Product','Region'])
# print(df)

# 3. Read a JSON file, limiting the number of rows
# df=pd.read_json('sample-weather-history.json')
# df=df.set_index('date')
# print(df.head(20))

# 4. Read an Excel file and convert it to a CSV file
df=pd.read_excel('FinancialSample.xlsx')
df.to_csv('FinancialSample.csv', index=False)