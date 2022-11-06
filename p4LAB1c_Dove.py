#CTI-110
#P4LAB1C
#Hayley Dove
#November 5, 2022
#
import turtle
wn = turtle.Screen()
snow = turtle.Turtle()
wn.title("p4LAB1c")

#Customizing Background and Pen
wn.bgcolor("dark blue")
snow.speed(20)

#Creating Snowflake 1
def branch():
    for i in range(3):
        for j in range(3):
            snow.forward(30)
            snow.backward(30)
            snow.right(45)
        snow.left(90)
        snow.backward(30)
        snow.left(45)
    snow.right(90)
    snow.forward(90)

for i in range(8):
    branch()
    snow.left(45)

#Moving Pen
snow.penup()
snow.forward(150)
snow.right(90)
snow.pendown()

#Creating Snowflake 2
for i in range(10):
        for j in range (2):
            snow.forward(50)
            snow.right(60)
            snow.forward(50)
            snow.right(120)
        snow.right(36)

#Moving Pen
snow.penup()
snow.forward(200)
snow.left(120)
snow.pendown()

#Creating Snowflake 3
def branch():
    for i in range(3):
        for j in range(3):
            snow.forward(10)
            snow.backward(10)
            snow.right(45)
        snow.left(90)
        snow.backward(10)
        snow.left(45)
    snow.right(90)
    snow.forward(30)

for i in range(8):
    branch()
    snow.left(45)
    

    
wn.exitonclick()
