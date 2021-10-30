import turtle
a=turtle.Turtle()
a.speed(100)
c=turtle.Screen()
c.bgcolor('black')
b=["red","blue","green","yellow","pink","orange","brown","green","blue","yellow","purple"]
a.color('brown')
a.up()
a.goto(-30,-30)
a.down()
for j in range(11):
    for i in range(50):
        a.forward(200)
        a.left(157)
    a.color(b[j])
    a.right(159)
    a.forward(100)
a.right (245)
a.forward(200)
a.color("white")
for j in range(1):
    for i in range(50):
        a.left(157)
        a.forward(200)
    a.right(159)
    a.forward(100)
    

