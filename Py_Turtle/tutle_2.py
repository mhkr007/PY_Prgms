import turtle
t=turtle.Pen()
#for i in range(0,1)
t.pencolor("green")
t.backward(270)  #size
t.right(90) #angle
t.backward(60)  #size
t.pencolor("orange")
t.backward(120)
t.right(90)
t.backward(270)  #size
t.right(90)

t.backward(180)  #size
t.right(90)
t.left(90)
#t.penup()###3
t.forward(60)
t.left(90)
t.forward(270)
t.right(90)
t.forward(60)
t.right(90)
#t.pendown()####
t.forward(270)
t.backward(135)
t.right(90)
t.forward(30)

#t.penup() #To draw invisible
#t=turtle.Pen()

t.pencolor("blue")

for i in range(0,24):
    t.right(75) 
    t.forward(30)
    t.backward(30)
