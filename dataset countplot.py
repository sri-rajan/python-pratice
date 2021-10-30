import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

a=pd.read_csv("dataset.csv")
b=a.head(20)
plt.figure(figsize=(15,32))
sb.countplot(y=b.Nationality,palette="Set2")
plt.show()
