import pandas as pd

data = {"Name": ["Asha", "Bala", "Charan"], "Score": [85, 90, 78]}
df = pd.DataFrame(data)
print(df)
print("Average Score:", df["Score"].mean())
