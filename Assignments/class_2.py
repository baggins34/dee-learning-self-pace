import pandas as pd
from scipy.stats import zscore

print("""
İbrahim Halil Bayat
Department of Electronics and Communication Engieering 
İstanbul Technical University 
İstanbul, Turkey 

Assignment 2 

""")

df = pd.read_csv("reg-33-data.csv")

print("Columns of the data frame: ", df.columns)

df['ratio'] = df['max'] / df['number']

print("\n--------- Dummies for 'cat2' -------------")
cat2_dummies = pd.get_dummies(df['cat2'])
df = pd.concat([df, cat2_dummies], axis=1)
df.drop("cat2", axis=1, inplace=True)

print("\n----------- Dummies for 'item' ---------------")
item_dummies = pd.get_dummies(df['item'])
df = pd.concat([df, item_dummies], axis=1)
df.drop("item", axis=1, inplace=True)

for column in df.columns:
    if column[0:2] == "CA":
        df["cat2_"+column] = df[column]
        df.drop(column, axis=1, inplace=True)
    elif column[0:2] == "IT":
        df["item_"+column] = df[column]
        df.drop(column, axis=1, inplace=True)


df['length'].fillna(df['length'].median(), inplace=True)
df['height'].fillna(df['height'].median(), inplace=True)
df['height'] = zscore(df['height'])
df.drop(["id", "convention", "usage", "region", "code", "power", "weight", "country", "target"],
        axis=1, inplace=True)
print("\nColumns of the last data frame: \n", df.columns)

df.to_csv("cleaned_data.csv")
# To check if the data has any NaN value
"""
for column in df.columns:
    print(f"{column} has na? {pd.isnull(df[column]).values.any()}")
"""