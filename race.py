import turtle
from turtle import *
from random import randint


screen = turtle.Screen()
screen.setup(800,600)
screen.bgcolor("orange")
screen.title("Race")

n1=screen.textinput("Player Name", "Name of first player:")
n2=screen.textinput("Player Name", "Name of second player:")
n3=screen.textinput("Player Name", "Name of third player:")
n4=screen.textinput("Player Name", "Name of fourth player:")

turtle.penup()
turtle.setx(-210)
turtle.sety(95)
turtle.write(n1)
turtle.pendown()

turtle.penup()
turtle.setx(-210)
turtle.sety(65)
turtle.write(n2)
turtle.pendown()

turtle.penup()
turtle.setx(-210)
turtle.sety(35)
turtle.write(n3)
turtle.pendown()

turtle.penup()
turtle.setx(-210)
turtle.sety(5)
turtle.write(n4)
turtle.pendown()

turtle.penup()
turtle.setx(-120)
turtle.sety(200)
turtle.write('Welcome to Turtle race!', font = ("CARDS", 18, "normal"))
turtle.pendown()

speed(10)
penup()
goto(-140,140)
pencolor("blue")
for a in range(21):
    write(a , align = 'left')
    right(90)
    forward(10)
    pendown()
    forward(150)
    penup()
    backward(160)
    left(90)
    forward(20)



ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,100)
ada.pendown()

ada1 = Turtle()
ada1.color('yellow')
ada1.shape('turtle')
ada1.penup()
ada1.goto(-160,70)
ada1.pendown()

ada2 = Turtle()
ada2.color('green')
ada2.shape('turtle')
ada2.penup()
ada2.goto(-160,40)
ada2.pendown()


ada3 = Turtle()
ada3.color('pink')
ada3.shape('turtle')
ada3.penup()
ada3.goto(-160,10)
ada3.pendown()

for turn in range(100):
    speed('normal')
    ada.forward(randint(1,8))
    ada1.forward(randint(1,8))
    ada2.forward(randint(1,8))
    ada3.forward(randint(1,8))
    
