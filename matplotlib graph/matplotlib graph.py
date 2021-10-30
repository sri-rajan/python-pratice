from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

x = [1,2,3,4,5,6]
y = [6,1,3,6,4,7]
x1 = [2,3,4,5,6,7]
y1 = [7,2,4,7,5,8]

plt.title('simple graph')

plt.xlabel('time')
plt.ylabel('work')

plt.plot(x,y,'g',label='line1',linewidth=20)
plt.plot(x1,y1,'c',label='line2',linewidth=5)

plt.grid(True,color='k')
plt.legend()

plt.show()
