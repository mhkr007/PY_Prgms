import turtle

t=turtle.Pen()
##window = turtle.getscreen()
##window.bgcolor("light blue")
#t.penup() #To draw invisible
#t=turtle.Pen()

t.pencolor("blue")
for i in range(0,24):  ## to draw spokes
    t.right(75) 
    t.forward(30)
    t.backward(30)
t.right(90)
t.forward(30)
t.color("green")### green
t.begin_fill()
t.right(90)
t.forward(135)
t.left(90)
t.forward(60)
t.left(90)
t.forward(270)
t.left(90)
t.forward(60)
t.left(90)
t.forward(135)
t.backward(135)
t.right(90)
t.end_fill()
t.color("white")
t.forward(60)
t.left(90)
t.pu()
t.forward(270)
t.left(90)
t.pendown()
t.forward(60)
t.backward(60)
t.color("orange")
t.begin_fill()
t.right(180)
t.forward(60)
t.right(90)
t.forward(270)
t.right(90)
t.forward(60)
t.right(90)
t.forward(270)
t.end_fill()

####stick
t.right(90)
t.pencolor("brown")
t.forward(60)
t.backward(400)
#######
##t.shapesize(4,1)
##t.shape("square")
##t.right(180)
##t.color("brown")
##t.begin_fill() ##begin_fill
##t.right(90)
###t.forward(100)
##t.right(90)
##t.forward(50)
##t.right(90)
##t.forward(20)
##t.right(90)
##t.forward(50)
##t.right(90)
##t.forward(20)
##t.right(90)
##t.end_fill()##end_fill
