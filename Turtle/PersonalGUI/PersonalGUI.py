import turtle as t

def f():
    t.pendown()

def u():
    t.penup()

def draw(x,y):
    t.setpos(x,y)

t.TurtleScreen.onkey(f,"f")
t.TurtleScreen.onkey(u,"u")
t.TurtleScreen.listen()

t.onscreenclick(draw)


t.mainloop()
