import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy import stats

a={"day":[1,2,3,4,5,6,7],"grocery":[30,80,45,23,51,46,76],"clothes":[13,40,34,23,54,67,98],
   "utensils":[12,32,27,23,14,35,39]}
b={"day":[8,9,10,11,12,13,14],"grocery":[30,80,45,23,51,46,76],"clothes":[13,40,34,23,54,67,98],
   "utensils":[12,32,27,23,14,35,39]}

x=pd.DataFrame(a)
y=pd.DataFrame(b)

mean,cov=[0,1],[(1,.5),(.5,1)]
data=np.random.multivariate_normal(mean,cov,200)
with sb.axes_style("white"):
    sb.jointplot(x=x,y=y,kind="kde",color="b");
plt.show()

#didn't work don't know why
#find later
