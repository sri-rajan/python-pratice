import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy import stats

flight = {"year":[1949,1949,1949,1949,1949,1949,1949,1949,1949,1949,1949,1949,
                  1950,1950,1950,1950,1950,1950,1950,1950,1950,1950,1950,1950,
                  1951,1951,1951,1951,1951,1951,1951,1951,1951,1951,1951,1951,
                  1952,1952,1952,1952,1952,1952,1952,1952,1952,1952,1952,1952,
                  1953,1953,1953,1953,1953,1953,1953,1953,1953,1953,1953,1953],
          "month":["jan","feb","mar","apr","may","jun","jul","aug","sep","oct",
                   "nov","dec",
                   "jan","feb","mar","apr","may","jun","jul","aug","sep","oct",
                   "nov","dec",
                   "jan","feb","mar","apr","may","jun","jul","aug","sep","oct",
                   "nov","dec",
                   "jan","feb","mar","apr","may","jun","jul","aug","sep","oct",
                   "nov","dec",
                   "jan","feb","mar","apr","may","jun","jul","aug","sep","oct",
                   "nov","dec",],
          "passenger":[112,115,118,128,114,125,135,130,114,117,119,113,
                       120,109,126,117,126,124,117,123,125,118,114,120,
                       118,128,114,125,135,130,114,117,119,113,120,109,
                       114,125,135,130,114,117,119,113,120,109,118,128,
                       126,124,117,123,125,125,135,130,114,117,119,122]}
flights = pd.DataFrame(flight)

sb.set(style="darkgrid",color_codes=True) # u can use .. dark,white,etc for style
sb.boxplot(x="month",y="passenger",data=flights)
plt.show()

sb.set(style="darkgrid",color_codes=True) # u can use .. dark,white,etc for style
sb.boxplot(x="month",y="passenger",data=flights)
sb.despine(offset=40,trim=True)
plt.show()
# see 9:50

d=sb.color_palette()
sb.palplot(d)
plt.show()



