import matplotlib.pyplot as plt

population = [22,33,64,34,64,23,65,77,12,112,76,87,34,97,99,43,68,86,35]
bins = [10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.hist(population,bins, histtype='bar',rwidth=0.8,label='population')

plt.legend()
plt.title('histogram')
plt.xlabel('time')
plt.ylabel('work')

plt.show()
