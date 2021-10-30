import turtle
a=turtle.Turtle()
a.speed(70)
b=turtle.Screen()
b.bgcolor('black')
a.color('blue')
for i in range(21):
    a.right(20)
    for j in range(4):
        a.forward(200)
        a.right(90)
a.color('yellow')
for i in range(21):
    a.right(20)
    for j in range(4):
        a.forward(25)
        a.right(90)
a.color('white')
for i in range(21):
    a.right(20)
    for j in range(4):
        a.forward(60)
        a.right(90)
a.color('red')
for i in range(21):
    a.right(20)
    for j in range(4):
        a.forward(120)
        a.right(90)

