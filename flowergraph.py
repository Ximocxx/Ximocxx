from turtle import *
def fleur():
    for i in range(300):
        circle(190-i,90)
        left(90)
        circle(190-i,90)
        left(18)
        speed(100) #change speed here

fleur()
mainloop()
