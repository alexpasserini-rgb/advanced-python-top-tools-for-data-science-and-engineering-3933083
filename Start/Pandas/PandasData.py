# Example file for Advanced Python: Top Tools for Data Science
# Performing Pandas data operations on a DataFrame


import pandas as pd


# Create a DataFrame from the sales data CSV file
df = pd.read_csv("sales_data.csv")


# 1. Sorting data by SalesAmount in descending order
# df=df.set_index("Product")
# df=df.sort_values(["Product","SalesAmount"],ascending=[True,False])
# print(df)

# 2. Filtering data for a specific region
# df=df[df["Region"]=="North"]
# print(df)

# 3. Filtering using calculated values
# mean_val=df["SalesAmount"].mean()
# print(mean_val)
# df=df[df["SalesAmount"]>mean_val]
# print(df)

# 4. Filtering using the isin() function
# df=df[df["Quarter"].isin(["Q1","Q2"])]
# print(df)

# 5. Filtering with the query function
# df=df.query("SalesAmount > 750 and Region != 'North'")
# print(df)

# 6. Grouping data by Product and calculating total sales
group_result=df.groupby("Product")
print(group_result["SalesAmount"].sum())