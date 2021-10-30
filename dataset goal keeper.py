import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

df=pd.read_csv("dataset.csv")

a= 0.5
b= 1
c= 2
d= 3

df["gk_Shot_Stopper"] = (b*df.Reactions+ b*df.Composure+a*df.SprintSpeed+a*df.Strength+c*df.Jumping+b*df.GKPositioning+c*df.GKDiving+d*df.GKReflexes+b*df.GKHandling)/(2*a+4*b+2*c+1*d)
df["gk_Sweeper"]= (b*df.Reactions+ b*df.Composure+b*df.SprintSpeed+a*df.LongShots+a*df.Jumping+b*df.GKPositioning+b*df.GKDiving+d*df.GKReflexes+b*df.GKHandling+d*df.GKKicking+c*df.Vision)/(2*a+5*b+2*d+a)

plt.figure(figsize=(9,5))
shot = df.sort_values("gk_Shot_Stopper",ascending=False)[:5]
x=np.array(list(shot["Name"]))
y=np.array(list(shot["gk_Shot_Stopper"]))

sb.barplot(x,y)
plt.ylabel("shot stopping score")

plt.show()

plt.figure(figsize=(9,5))
shot = df.sort_values("gk_Sweeper",ascending=False)[:5]
x=np.array(list(shot["Name"]))
y=np.array(list(shot["gk_Sweeper"]))

sb.barplot(x,y)
plt.ylabel("shot stopping score")

plt.show()
