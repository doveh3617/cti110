#CTI-110
#P4LAB1B
#Hayley Dove
#November 5, 2022
#
import turtle
wn = turtle.Screen()
hd = turtle.Turtle()
wn.title("p4LAB1b")

#Customizing Background and Pen
wn.bgcolor("LavenderBlush")
hd.pencolor("hot pink")
hd.pensize(20)

#Creating H
hd.right(90)

hd.forward(100)
hd.backward(200)
hd.forward(100)
hd.right(90)
hd.forward(150)
hd.left(90)
hd.forward(100)
hd.backward(200)

#Moving Pen
hd.penup()
hd.left(90)
hd.forward(300)
hd.right(90)
hd.forward(200)
hd.left(90)
hd.pendown()

#Creating D
hd.circle(100,180)
hd.left(90)
hd.forward(190)

wn.exitonclick()
