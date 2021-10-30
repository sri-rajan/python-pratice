import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

a=pd.read_csv("dataset.csv")

plt.figure(figsize=(8,5))
sb.countplot(x="Age",data=a)
plt.title("countplot",color="red")
plt.show()

