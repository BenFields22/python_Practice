import turtle as t
def printxy(x,y):
    print(x,y)


t.setup(300,200)
t.screensize(300,200)
t.setworldcoordinates(0,0,300,200)

t.penup()
t.setpos(100,0)
t.pendown()
t.setpos(100,200)
t.penup()
t.setpos(200,0)
t.pendown()
t.setpos(200,200)

def square(length):
    for i in range(4):
        t.fd(length)
        t.left(90)

def shapedrawer(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    t.begin_fill()
    if x <= 100:
        t.color('green')
        square(10)
    elif 100< x <= 200:
        t.color('red')
        t.circle(10)
    else:
        t.color('blue')
        square(10)
    t.end_fill()

t.onscreenclick(shapedrawer)
t.mainloop()









