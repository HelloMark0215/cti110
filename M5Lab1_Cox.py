#CTI-110
#M5Lab1
#William Cox
#22 October 2017

import turtle
triangle = turtle
square = turtle
triangle.shape("turtle")
square.shape("turtle")

for acolor in ["yellow","red","blue","green"]:
    square.color(acolor)
    square.forward(90)
    square.right(90)
    
turtle.up()
turtle.goto(0,100)
turtle.down()
for acolor in ["red","blue","green"]:
    triangle.color(acolor)
    triangle.forward(100)
    triangle.right(120)

