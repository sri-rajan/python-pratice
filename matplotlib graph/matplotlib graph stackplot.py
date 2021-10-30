import matplotlib.pyplot as plt

days = [1,2,3,4,5,6]

sleeping = [6,8,7,5,11,12]
eating = [3,5,4,1,5,6]
working = [7,4,8,6,8,5]
playing = [7,9,6,9,11,13]

plt.plot([],[],color='m',label='sleeping',linewidth=5)
plt.plot([],[],color='c',label='eating',linewidth=5)
plt.plot([],[],color='r',label='working',linewidth=5)
plt.plot([],[],color='k',label='playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing, colors=['m','c','r','k'])

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("stackplot")
plt.legend()

plt.show()


