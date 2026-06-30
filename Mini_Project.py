import pandas as pd
student = {
    "Name" : ["Sumant",None,"Raja","Abhi","Pritam","Prakash","Abhi"],
    "Age" : [20,21,34,43,None,None,43],
    "Mark" : [95,92,88,85,None,89,85]
}
df = pd.DataFrame(student)

print("Original Dataset:")
print(df)
print("\nCounting null values:")
print(df.isnull().sum())
df = df.drop_duplicates()
print("\nAfter removing  duplicate Values:")
print(df)
df["Mark"] = df["Mark"].fillna(df["Mark"].mean())
print("\nAfter Filling missing Mark:")
print(df)
df = df.rename(columns={"Mark" : "Score"})
print("\nAfter Renaming Column Mark to Score:")
print(df)
df["Name"] = df["Name"].fillna("Unknown")
print("\nAfter filling missing Name:")
print(df)
df["Age"] = df["Age"].fillna(df["Age"].mean())
print("\nAfter filling missing Age:")
print(df)
print("\nCleaned DataSet:")
print(df)