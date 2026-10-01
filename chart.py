import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")
df.plot(x="Name", y="Score", kind="bar")
plt.show(