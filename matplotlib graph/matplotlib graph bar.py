import matplotlib.pyplot as plt

plt.bar([1,3,5,7,9,11],[6,1,3,6,4,7], label='line1',color='g')
plt.bar([2,4,6,8,10,13],[7,2,4,7,5,8], label='line2')


plt.title('simple graph')

plt.legend()
plt.xlabel('time')
plt.ylabel('work')

plt.show()
