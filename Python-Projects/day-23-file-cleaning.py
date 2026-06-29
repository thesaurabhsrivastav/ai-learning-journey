import pandas as pd
import numpy as np

data = {
    "Name": ["Rahul", "Aman", "Priya"],
    "Marks": [90, np.nan, 95]
}

df = pd.DataFrame(data)

print(df)

print(df.isnull())

print(df.isnull().sum())

df = df.dropna() #Removes Missing Values

data = {
    "Name": ["Rahul", "Aman", "Priya"],
    "Marks": [90, np.nan, 95]
}

df = pd.DataFrame(data)

df["Marks"] = df["Marks"].fillna(0) #Fill Missing Values

df["Marks"] = df["Marks"].fillna(df["Marks"].mean()) #Fill Using avg

data = {
    "Name": ["Rahul", "Rahul", "Aman"],
    "Marks": [90, 90, 85]
}

print(df.duplicated())

df = df.drop_duplicates()

df.rename(columns={"Marks": "Score"}, inplace=True)