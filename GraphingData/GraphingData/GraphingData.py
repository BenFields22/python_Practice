import turtle
import random

def draw(x,y):
    turtle.setpos(x,y)
prompt = input('Please press ENTER to see the performance data from your last workout')

turtle.tracer(0,0)

dashlinesy = [0,10,20,30,40,50,60,70,80,90,100]
dashlinesx = [0,1,2,3,4,5,6,7,8,9,10]

HR = random.sample(range(101),10)
time = [1,2,3,4,5,6,7,8,9,10]
MaxHR = HR[0]
workoutDur = 10 #minutes
count = 1

for i in range(len(HR)):
    #print(numbers[i])

    if HR[i] >= MaxHR:
        MaxHR = HR[i]
        maxtime = count
    count+=1



xMax = workoutDur + 2
yMax = MaxHR + 20
turtle.getscreen()
turtle.Screen().setworldcoordinates(-2,-10,xMax,yMax)
turtle.Screen().title("Workout Data")


#draw dash marks in the y direction
for i in dashlinesy:
    if i == 0:
        turtle.penup()
        turtle.pensize(10)
        turtle.color('black')
        turtle.setpos(-2,0)
        turtle.pendown()
        turtle.setpos(12,0)
        turtle.pensize(1)
    else:
        turtle.penup()
        turtle.color('black')
        turtle.setpos(0,i)
        turtle.pendown()
        turtle.setpos(10,i)
        turtle.penup()
        turtle.setpos(-2,55)
        turtle.pendown()
        turtle.write('HeartRate\n(BPM)',font=(16))
        turtle.penup()
        turtle.setpos(-.7,i)
        turtle.pendown()
        turtle.write(i,font=(16))
        turtle.penup()

#set dashed lines for the x direction
for j in dashlinesx:
    if j == 0:
        turtle.penup()
        turtle.setpos(-1,1)
        turtle.pendown()
        #turtle.write('X',font=(16))
        turtle.penup()
        turtle.pensize(10)
        turtle.color('black')
        turtle.setpos(0,-10)
        turtle.pendown()
        turtle.setpos(0,120)
        turtle.pensize(1)
    else:
        turtle.penup()
        turtle.setpos(j,-4)
        turtle.pendown()
        turtle.write(j*10,font=(16))
        turtle.penup()
        turtle.color('black')
        turtle.setpos(j,0)
        turtle.pendown()
        turtle.setpos(j,100)
        turtle.penup()
        turtle.setpos(5,-10)
        turtle.pendown()
        turtle.write('Time(minutes)',font=(16))
        turtle.penup()

turtle.color('red')
turtle.pensize(3)
turtle.update()


turtle.setpos(0,0)
turtle.pendown()
turtle.speed(3)
turtle.update()
turtle.tracer(1)
for i in range(len(HR)):
    dataY = HR[i]
    dataX = time[i]
    turtle.setpos(dataX,dataY)

turtle.tracer(0)

turtle.penup()
turtle.setpos(maxtime,MaxHR-1)
turtle.pendown()
turtle.color('black')
turtle.forward(.1)
turtle.left(90)
turtle.forward(2)
turtle.left(90)
turtle.forward(.2)
turtle.left(90)
turtle.forward(2)
turtle.left(90)
turtle.forward(.1)
turtle.penup()
turtle.setpos(maxtime-1,MaxHR+2)
turtle.write('Max Heart Rate: %s'%MaxHR,font=(16))
turtle.penup()


turtle.hideturtle()


turtle.update()


turtle.Screen().exitonclick()





