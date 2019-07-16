import turtle
t=turtle.Pen()
colors=['red','green','purple','blue','orange','black']
for i in range(101):
    t.pencolor(colors[i%5])
    t.width(i/10+1)
    t.forward(i)
    t.left(59)
