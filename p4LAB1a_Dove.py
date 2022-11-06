#CTI-110
#P4LAB1A
#Hayley Dove
#November 5, 2022
#
import turtle
wn = turtle.Screen()
square = turtle.Turtle()
triangle = turtle.Turtle()
wn.title("p4LAB1a")

#Customize Background and Pens
wn.bgcolor("grey86")
square.color("blue")
triangle.color("green")

#Create Square
for i in range(4):
    square.left(90)
    square. forward(50)

#Create Triangle
for i in range(3):
    triangle.left(120)
    triangle. forward(80)

wn.exitonclick()
