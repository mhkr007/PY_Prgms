import turtle

t=turtle.Pen()


#t.penup() #To draw invisible
#t=turtle.Pen()

t.pencolor("blue")
for i in range(0,24):  ## to draw spokes
    t.right(75) 
    t.forward(30)
    t.backward(30)
t.right(90)
t.forward(30)
t.pencolor("green")### green
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
t.pencolor("black")
t.forward(60)
t.left(90)
t.penup()
t.forward(270)
t.left(90)
t.pendown()
t.forward(60)
t.backward(60)
t.pencolor("orange")
t.right(180)
t.forward(60)
t.right(90)
t.forward(270)
t.right(90)
t.forward(60)
t.right(90)
t.forward(270)
t.left(90)
t.penup()
t.forward(120)
t.pendown()
t.pencolor("brown")
t.forward(240)

###for i in range(0,1)
##t.pencolor("green")
##t.forward(270)  #size
##t.right(90) #angle
