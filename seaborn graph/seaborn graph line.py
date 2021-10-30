import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

flight = {"month":[1,2,3,4,5,6,7,8],
          "passenger":[10,12,14,16,18,20,22,24]}
flights = pd.DataFrame(flight)
print(flights)

sb.relplot(x="passenger",y="month",data=flights,kind="line")
plt.show()
