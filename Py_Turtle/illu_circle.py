#circle with angle
##from turtle import *
##pencolor("green")
##for angle in range(0, 360, 20):
##    setheading(angle)
##    forward(100)
##    write(str(angle) + '*')
##    backward(45)

#flower of life
from turtle import *
pencolor("red")
circle_size = 50
for i in range(6):
    circle(circle_size)
    left(60)
pencolor("violet")

for i in range(100):
    forward(i)
    left(91)
bye()
#to draw home
##from turtle import *
##pencolor("red")
##goto(500, 0)
##goto(500, 400)
##goto(50, 400)
##goto(0, 300)
##goto(0, 0)
##penup()
##goto(50, 400)
##pendown()
##goto(100, 300)
##goto(100, 0)
##penup()
##goto(0, 300)
##pendown()
##goto(100, 300)
##goto(500, 300)
##screensize(2000, 2000) #increase the screen size to fit the figure
