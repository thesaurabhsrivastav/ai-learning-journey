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
    "Name": ["Rahul", "Rahul", "Aman", "Saurabh"],
    "Marks": [90, 90, 85, 70]
}

df = pd.DataFrame(data)

print(df.duplicated())

print(df["Marks"].unique())

print(df["Marks"].nunique())

print(df["Marks"].value_counts())

df = df.drop_duplicates()

df.rename(columns={"Marks": "Score"}, inplace=True)
