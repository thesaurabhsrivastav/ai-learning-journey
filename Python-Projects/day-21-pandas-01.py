import pandas as pd

marks = pd.Series([70, 80, 90, 95]) #Series is Single column of data

print(marks)

data = {

    "Name": ["Rahul", "Aman", "Priya"],

    "Marks": [90, 85, 95]

}

df = pd.DataFrame(data)

print(df)

print("Head:", df.head(1)) #Check the First Row
print("Info:",df.info())
print(df["Marks"])

students = [
    ["Rahul", 90],
    ["Aman", 85],
    ["Priya", 95]
]

df = pd.DataFrame(
    students,
    columns=["Name", "Marks"]
)

print(df)


data = {
    "Name": ["Rahul", "Aman", "Priya", "Rohit"],
    "Marks": [90, 85, 95, 88]
}

df = pd.DataFrame(data)

print(df)
df[df["Marks"] > 90]
df.sort_values()
df[["Name", "Marks"]]
df.loc[0, "Marks"] = 100

print(df)