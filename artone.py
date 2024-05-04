import turtle
turtle.bgcolor('black')
t = turtle.Turtle()
colors = ['red', 'dark red'] #change color here
turtle.speed(10) #change speed here
for number in range(400):
    t.forward(number+1)
    t.right(89)
    t.pencolor(colors[number%2])
