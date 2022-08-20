"""
Program: Turtle Graphic Game
Date: 20/08/2022

"""
import turtle
import math
import random

#Set-up the turtle screen
wn = turtle.Screen()
wn.title("My Turtle Game")
wn.bgcolor("black")
# wn.bgpic("sky.gif")
wn.setup(width=600, height=600)
wn.tracer()

#Draw the border
border = turtle.Turtle()
border.color("white")
border.penup()
border.setposition(-280, -280)
border.pendown()
border.pensize(3)
border.speed(6)
for side in range(4):
    border.forward(560)
    border.left(90)
border.hideturtle()

#create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
#player.turtlesize()
player.penup()
player.speed(0)

#Create a score variable
score = 0


#Create Multiple goals
maxGoals = 10
goals = []
colors = ["red", "green", "blue", "yellow", "gray", "lightblue", "purple", "cyan", "orange", "tomato"]

for count in range(maxGoals):
    # Create a task/goal
    goals.append(turtle.Turtle())
    goals[count].color(colors[count%maxGoals])
    goals[count].shape('circle')
    goals[count].penup()
    goals[count].speed(9)
    # put the goal in a particular position when we start the game
    # goal.setposition(-200,-200)
    goals[count].setposition(random.randint(-260, 260), random.randint(-260, 260))


#Set speed variable
speed = 1

#Define Functions
def turnleft():
    player.left(30)
def turnright():
    player.right(30)

def increasespeed():
    global speed
    speed += 1
def decreasespeed():
    global speed
    speed -= 1

#A function that takes 2 turtle objects and decides if there is a collison
def isCollision(player, goal):
    d = math.sqrt(math.pow(player.xcor() - goal.xcor(), 2) + math.pow(player.ycor() - goal.ycor(), 2))
    if d < 20:
        return True
    else:
        return False

#Bind keyboard to functions
turtle.listen()     #set focust to the screen and look for key presence
turtle.onkey(turnleft, "Left")         #listens for the user to press a certain key
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(decreasespeed, "Down")

while True:
    player.forward(speed)
    #Boundary Checking
    if player.xcor() > 270 or player.xcor() < -270:
        player.right(180)
        #play sound

    if player.ycor() > 270 or player.ycor() < -270:
        player.right(180)
        #play sound (bounce)

    #Move the goal
    for count in range(maxGoals):
        goals[count].forward(5)

         # Set Boundary for the goal
        if goals[count].xcor() > 270 or goals[count].xcor() < -270:
            goals[count].right(180)
            #play sound (bounce)

        if goals[count].ycor() > 270 or goals[count].ycor() < -270:
            goals[count].right(180)
            #play sound (bounce)

        # Collision Checking
        if isCollision(player, goals[count]):
         # goal.hideturtle() #This is to hide the turtle after collision with the player
            goals[count].setposition(random.randint(-260, 260), random.randint(-260, 260))
            goals[count].right(random.randint(0, 360))
            #play sound(collison)
            score += 1
            print(score)
            #Draw score on the screen(using border pen)
            border.undo()
            border.penup()
            border.hideturtle()
            border.setposition(-270,280)
            scorestring = f"Score: {score}"
            border.write(scorestring, align="left", font=("ds-digital",15, "bold"))



wn.mainloop()   #to keep the window open