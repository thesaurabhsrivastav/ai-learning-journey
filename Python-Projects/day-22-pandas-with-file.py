import pandas as pd

df = pd.read_csv("student_records.csv")

print(df)
print(df.shape)
print(df.columns)
print(df.info())
df["Passed"] = df["Marks"] >= 40
df.to_csv("students_updated.csv", index=False)