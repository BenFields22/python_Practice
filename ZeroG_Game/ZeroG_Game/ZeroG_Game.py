#game that simulates a zero gravity environment

import turtle
import math
import random
import time

elapsed = 0
gamestate = 'beginning'

sc = turtle.Screen()
sc.title('ZeroG')
#sc.bgcolor('black')
sc.bgpic('space2.gif')

#turtle.register_shape('dogship.gif')
turtle.register_shape('astro_mario.gif')

global player
player = turtle.Turtle()

#player.shape('dogship.gif')
player.shape('turtle')
player.shapesize(2)
player.color('red')
x = 0
y = 0
player.penup()
player.setpos(280,-245)

#create timer
timePen = turtle.Turtle()
timePen.hideturtle()
timePen.color('white')
timePen.penup()
timePen.setpos(-300,220)
elapsed = 0
timeString = 'Elapsed Time: '
timePen.write(timeString,align = 'left',font=('Arial',16))
timePen.penup()

TimerPen= turtle.Turtle()
TimerPen.hideturtle()
TimerPen.color('white')
TimerPen.penup()
TimerPen.setpos(-200,220)
elapsed = 0
TimerPen.write(elapsed,align='Left',font=('Arial',16))
TimerPen.penup()


#create cargo

numCargo = 4
cargos = []
startx = -400
starty = 200

for cargo in range(numCargo):
    startx += 150
    starty += 0
    cargo = turtle.Turtle()
    cargo.hideturtle()
    cargo.shape('astro_mario.gif')
    cargo.color('yellow')
    cargo.shapesize(1,1)
    cargo.penup()
    #cargo.setpos(startx,starty)
    #cargo.showturtle()
    cargos.append(cargo)
cargos[0].setpos(random.randint(-300,300),random.randint(-200,200))
cargos[1].setpos(random.randint(-300,300),random.randint(-200,200))
cargos[2].setpos(random.randint(-300,300),random.randint(-200,200))
cargos[3].setpos(random.randint(-300,300),random.randint(-200,200))
for i in range(4):
    cargos[i].showturtle()


#draw platform
scenePen = turtle.Turtle()
scenePen.speed(0)
scenePen.hideturtle()
scenePen.penup()
scenePen.color('white')
scenePen.setpos(-270,-260)
scenePen.pendown()
scenePen.begin_fill()
scenePen.fillcolor('green')
scenePen.fd(30)
scenePen.right(90)
scenePen.fd(10)
scenePen.right(90)
scenePen.fd(30)
scenePen.right(90)
scenePen.fd(10)
scenePen.end_fill()
scenePen.penup()

#draw platform
scenePen = turtle.Turtle()
scenePen.speed(0)
scenePen.hideturtle()
scenePen.penup()
scenePen.color('white')
scenePen.setpos(270,-260)
scenePen.pendown()
scenePen.begin_fill()
scenePen.fillcolor('orange')
scenePen.fd(30)
scenePen.right(90)
scenePen.fd(10)
scenePen.right(90)
scenePen.fd(30)
scenePen.right(90)
scenePen.fd(10)
scenePen.end_fill()
scenePen.penup()

bulletNum = 1

pHeading = 90
player.setheading(pHeading)
global xMov
xMov = 0
global yMov
yMov = 0

global pSpeed
pSpeed = .5

scorePen = turtle.Turtle()
scorePen.speed(0)
scorePen.color('white')
scorePen.penup()

scorePen.setpos(-300,280)
XVel = 'X-Velocity %.2f' %xMov

YVel = 'Y-Velocity %.2f' %yMov

BosPow = 'Booster Power %.2f' %pSpeed

scorePen.write(XVel,False,align ='left',font=('arial',16))
scorePen.penup()
scorePen.setpos(-300,260)
scorePen.write(YVel,False,align ='left',font=('arial',16))
scorePen.setpos(-300,240)
scorePen.write(BosPow,False,align ='left',font=('arial',16))
scorePen.hideturtle()

#cargo collection prompt
cargoPen = turtle.Turtle()
cargoPen.hideturtle()
cargoPen.color('yellow')
cargoPen.penup()
cargoPen.setpos(150,280)
cargoLeft = 0
cargoprompt = ' Cargo Collected {0}/{1}'.format(cargoLeft,numCargo)
cargoPen.write(cargoprompt,False,align ='left',font=('arial',16))
cargoPen.penup()

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 30:
        global cargoLeft
        global numCargo
        cargoLeft +=1
        if cargoLeft <=0:
            cargoLeft = 0
        if cargoLeft == 4:
            cargoPen.color('green')
        cargoPen.clear()
        cargoprompt = ' Cargo Collected {0}/{1}'.format(cargoLeft,numCargo)
        cargoPen.write(cargoprompt,False,align ='left',font=('arial',16))
        cargoPen.penup()
        return True
    else:
        return False

def RightArrow():
    if gamestate != 'beginning'and gamestate != 'complete':
        global pHeading
        pHeading = pHeading -30
        if pHeading < 0:
            pHeading = 360 + pHeading
        if pHeading > 360:
            pHeading = pHeading-360
        player.setheading(pHeading)

def LeftArrow():
    if gamestate != 'beginning'and gamestate != 'complete':
        global pHeading
        pHeading = pHeading +30
        if pHeading < 0:
            pHeading = 360 - pHeading
        if pHeading > 360:
            pHeading = pHeading-360
        player.setheading(pHeading)
def UpArrow():
    global gamestate
    if gamestate != 'complete':
        gamestate = 'started'
        global now
        now = time.time()+-elapsed
        global pSpeed
        global xMov
        global yMov
        #pSpeed +=1

        if pHeading < 90 and pHeading > 0:
            xMov = pSpeed* math.cos(math.radians(pHeading))+xMov
            yMov = pSpeed* math.sin(math.radians(pHeading))+yMov
            x = player.xcor()
            y = player.ycor()
            x = x+ xMov
            y = y+ yMov

        elif pHeading == 0 or pHeading == 360:
            xMov = pSpeed+xMov
            yMov = 0+yMov
            x = player.xcor()
            y = player.ycor()
            x = x + xMov
            y = y+ yMov
        elif pHeading == 90:
            xMov=0+xMov
            yMov=pSpeed + yMov
            x = player.xcor()
            y = player.ycor()
            x = x+ xMov
            y = y+ yMov
        elif pHeading > 90 and pHeading < 180:
            xMov = pSpeed* math.cos(math.radians(pHeading))+xMov
            yMov = pSpeed* math.sin(math.radians(pHeading))+yMov
            x = player.xcor()
            y = player.ycor()
            x = x+ xMov
            y = y+ yMov
        elif pHeading == 180:
            xMov = -pSpeed+xMov
            yMov = 0 + yMov
            x = player.xcor()
            y = player.ycor()
            x = x + xMov
            y = y+ yMov
        elif pHeading > 180 and pHeading < 270:
            xMov = pSpeed* math.cos(math.radians(pHeading))+ xMov
            yMov = pSpeed* math.sin(math.radians(pHeading))+ yMov
            x = player.xcor()
            y = player.ycor()
            x = x+ xMov
            y = y+ yMov
        elif pHeading==270:
            xMov = 0+ xMov
            yMov = -pSpeed + yMov
            x = player.xcor()
            y = player.ycor()
            x = x + xMov
            y = y+ yMov
        elif pHeading > 270 and pHeading < 360:
            xMov = pSpeed* math.cos(math.radians(pHeading))+xMov
            yMov = pSpeed* math.sin(math.radians(pHeading))+yMov
            x = player.xcor()
            y = player.ycor()
            x = x+ xMov
            y = y+ yMov

        #player.setpos(x,y)
        #print('X-Velocity: ',xMov)
        #print('Y-Velocity: ',yMov)
        #print('X-Cord: ',x)
        #print('Y-Cord: ',y)
        #print('Heading',pHeading,'Degrees')

        scorePen.clear()
        scorePen.setpos(-300,280)
        XVel = 'X-Velocity %.2f' %xMov
        YVel = 'Y-Velocity %.2f' %yMov
        BosPow = 'Booster Power %.2f' %pSpeed
        scorePen.write(XVel,False,align ='left',font=('arial',16))
        scorePen.penup()
        scorePen.setpos(-300,260)
        scorePen.write(YVel,False,align ='left',font=('arial',16))
        scorePen.setpos(-300,240)
        scorePen.write(BosPow,False,align ='left',font=('arial',16))
        scorePen.hideturtle()

def DownArrow():
    global pSpeed
    global xMov
    global yMov
    if gamestate != 'beginning'and gamestate != 'complete':
        if pHeading < 90 and pHeading > 0:
            xMov = -pSpeed* math.cos(math.radians(pHeading))+xMov
            yMov = -pSpeed* math.sin(math.radians(pHeading))+yMov
            x = player.xcor()
            y = player.ycor()
            x = x- xMov
            y = y- yMov

        elif pHeading == 0 or pHeading == 360:
            xMov = -pSpeed+xMov
            yMov = -0+yMov
            x = player.xcor()
            y = player.ycor()
            x = x - xMov
            y = y- yMov
        elif pHeading == 90:
            xMov=-0+xMov
            yMov=-pSpeed + yMov
            x = player.xcor()
            y = player.ycor()
            x = x- xMov
            y = y- yMov
        elif pHeading > 90 and pHeading < 180:
            xMov = -pSpeed* math.cos(math.radians(pHeading))+xMov
            yMov = -pSpeed* math.sin(math.radians(pHeading))+yMov
            x = player.xcor()
            y = player.ycor()
            x = x- xMov
            y = y- yMov
        elif pHeading == 180:
            xMov = pSpeed+xMov
            yMov = 0 + yMov
            x = player.xcor()
            y = player.ycor()
            x = x - xMov
            y = y- yMov
        elif pHeading > 180 and pHeading < 270:
            xMov = -pSpeed* math.cos(math.radians(pHeading))+ xMov
            yMov = -pSpeed* math.sin(math.radians(pHeading))+ yMov
            x = player.xcor()
            y = player.ycor()
            x = x- xMov
            y = y- yMov
        elif pHeading==270:
            xMov = 0+ xMov
            yMov = pSpeed + yMov
            x = player.xcor()
            y = player.ycor()
            x = x - xMov
            y = y- yMov
        elif pHeading > 270 and pHeading < 360:
            xMov = -pSpeed* math.cos(math.radians(pHeading))+xMov
            yMov = -pSpeed* math.sin(math.radians(pHeading))+yMov
            x = player.xcor()
            y = player.ycor()
            x = x- xMov
            y = y- yMov

        #player.setpos(x,y)
       # print('X-Velocity: ',xMov)
        #print('Y-Velocity: ',yMov)
        #print('X-Cord: ',x)
        #print('Y-Cord: ',y)
        #print('Heading',pHeading,'Degrees')

        scorePen.clear()
        scorePen.setpos(-300,280)
        XVel = 'X-Velocity %.2f' %xMov
        YVel = 'Y-Velocity %.2f' %yMov
        BosPow = 'Booster Power %.2f' %pSpeed
        scorePen.write(XVel,False,align ='left',font=('arial',16))
        scorePen.penup()
        scorePen.setpos(-300,260)
        scorePen.write(YVel,False,align ='left',font=('arial',16))
        scorePen.setpos(-300,240)
        scorePen.write(BosPow,False,align ='left',font=('arial',16))
        scorePen.hideturtle()

def increaseBoost():
    global pSpeed
    pSpeed += .1
    scorePen.clear()
    scorePen.setpos(-300,280)
    XVel = 'X-Velocity %.2f' %xMov
    YVel = 'Y-Velocity %.2f' %yMov
    BosPow = 'Booster Power %.2f' %pSpeed
    scorePen.write(XVel,False,align ='left',font=('arial',16))
    scorePen.penup()
    scorePen.setpos(-300,260)
    scorePen.write(YVel,False,align ='left',font=('arial',16))
    scorePen.setpos(-300,240)
    scorePen.write(BosPow,False,align ='left',font=('arial',16))
    scorePen.hideturtle()

def decreaseBoost():
    global pSpeed
    pSpeed -= .1
    scorePen.clear()
    scorePen.setpos(-300,280)
    XVel = 'X-Velocity %.2f' %xMov
    YVel = 'Y-Velocity %.2f' %yMov
    BosPow = 'Booster Power %.2f' %pSpeed
    scorePen.write(XVel,False,align ='left',font=('arial',16))
    scorePen.penup()
    scorePen.setpos(-300,260)
    scorePen.write(YVel,False,align ='left',font=('arial',16))
    scorePen.setpos(-300,240)
    scorePen.write(BosPow,False,align ='left',font=('arial',16))
    scorePen.hideturtle()
def shoot():
    bulletspeed = 30
    bullet = turtle.Turtle()
    bullet.penup()
    bullet.hideturtle()
    bullet.shape('circle')
    bullet.color('yellow')
    xb = player.xcor()
    yb = player.ycor()
    bullet.setpos(xb,yb)
    bullet.showturtle()
    bullet.setheading(pHeading)

#assign key commands
turtle.listen()
turtle.onkey(RightArrow,'Right')
turtle.onkey(LeftArrow,'Left')
turtle.onkey(UpArrow,'Up')
turtle.onkey(decreaseBoost,'1')
turtle.onkey(increaseBoost,'2')
turtle.onkey(DownArrow,'Down')
turtle.onkey(shoot,'space')

#prompt the user on the objective
promptPen = turtle.Turtle()
promptPen.speed(0)
promptPen.hideturtle()
promptPen.penup()
promptPen.color('white')
promptPen.setpos(-280,-100)
promptPen.pendown()
promptPen.begin_fill()
promptPen.fillcolor('black')
promptPen.setpos(280,-100)
promptPen.setpos(280,100)
promptPen.setpos(-280,100)
promptPen.setpos(-280,-100)
promptPen.end_fill()
promptPen.penup()
promptPen.setpos(0,0)
promptPen.write('Save the Lost Astronauts and Land on the Green Cargo Dock\nUse arrow keys to initiate boosters for navigation\nAdjust booster power using "1" and "2"\nTurn using the "left" and "Right" arrow keys',align='center',font=('arial',20))

gameloop = True
watch = 1
while gameloop:
    if gamestate == 'started':
        promptPen.clear()
        current = time.time()
        global now
        global elapsed
        elapsed = (current - now)
        if elapsed > watch:
            TimerPen.clear()
            watch +=1
            TimerPen.write('%.0f'%elapsed,align='Left',font=('Arial',16))
            TimerPen.penup()
            #print(elapsed)
    x = player.xcor()
    y = player.ycor()
    x = x+xMov
    y = y+yMov
    player.setpos(x,y)
    for cargo in cargos:
        if isCollision(player,cargo):
            cargo.hideturtle()
            cargo.setpos(400,200)
    if x >330 or x < -330:
        xMov = xMov *-1
        scorePen.clear()
        scorePen.setpos(-300,280)
        XVel = 'X-Velocity %.2f' %xMov
        YVel = 'Y-Velocity %.2f' %yMov
        BosPow = 'Booster Power %.2f' %pSpeed
        scorePen.write(XVel,False,align ='left',font=('arial',16))
        scorePen.penup()
        scorePen.setpos(-300,260)
        scorePen.write(YVel,False,align ='left',font=('arial',16))
        scorePen.setpos(-300,240)
        scorePen.write(BosPow,False,align ='left',font=('arial',16))
        scorePen.hideturtle()

    if y >330 or y<-330:
        yMov=yMov*-1
        scorePen.clear()
        scorePen.setpos(-300,280)
        XVel = 'X-Velocity %.2f' %xMov
        YVel = 'Y-Velocity %.2f' %yMov
        BosPow = 'Booster Power %.2f' %pSpeed
        scorePen.write(XVel,False,align ='left',font=('arial',16))
        scorePen.penup()
        scorePen.setpos(-300,260)
        scorePen.write(YVel,False,align ='left',font=('arial',16))
        scorePen.setpos(-300,240)
        scorePen.write(BosPow,False,align ='left',font=('arial',16))
        scorePen.hideturtle()

    if y <= -245 and y>= -255 and x >=-270 and x <= -240: #and gamestate!= 'beginning':
        if pHeading != 90 and yMov >-.5 and yMov <0:
            yMov = yMov*-1
            continue
        player.setpos(x,-245)
        if yMov < -.8:
            gamestate = 'failure'
            break
        if cargoLeft ==4:
            xMov = 0
            yMov = 0
            scorePen.setpos(0,0)
            gamestate = 'complete'
            break

if gamestate == 'failure':
    scorePen.setpos(0,0)
    scorePen.write('Mission Failure\nHigh Docking\n Speed',align='center',font=('arial',30))
if gamestate == 'complete':
    scorePen.setpos(0,0)
    scorePen.color('white')
    scorePen.write('Mission Complete',align='center',font=('arial',30))
    TimerPen.write('%.2f'%elapsed,align='Left',font=('Arial',16))
    TimerPen.penup()
turtle.mainloop()