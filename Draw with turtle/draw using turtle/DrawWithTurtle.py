#code to practice looping events

import turtle 


def main():
    numsides= int(input('Please enter the number of sides you want your shape to have: '))


    for steps in range(numsides) :
        turtle.forward(100)
        turtle.right(360/numsides)
        for moresteps in range(numsides):
            turtle.forward(50)
            turtle.right(360/numsides)




if __name__ == "__main__":
    main()