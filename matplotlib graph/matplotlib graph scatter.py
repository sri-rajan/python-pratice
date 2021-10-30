import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7]
y = [5,9,2,3,7,1,8]

plt.scatter(x,y,label='values',color='k')

plt.title('scatter')
plt.xlabel('time')
plt.ylabel('work')
plt.legend()

plt.show()
