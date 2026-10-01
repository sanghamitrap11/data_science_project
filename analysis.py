import pandas as pd

data = {"Name": ["Asha", "Bala", "Charan"], "Score": [85, 90, 78]}
df = pd.DataFrame(data)
print(df)
print("Average Score:", df["Score"].mean())
print("Maximum Score:", df["Score"].max())
print("Minimum Score:", df["Score"].min())
