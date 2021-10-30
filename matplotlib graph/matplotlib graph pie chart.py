import matplotlib.pyplot as plt

slices = [7,2,2,4]
activities = ["sleeping","eating","working","playing"]
cols = ['r','b','c','m']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow=True,
        explode=(0,0,0.1,0),
        autopct="%1.1f%%")

plt.title("pie chart")

plt.show()


