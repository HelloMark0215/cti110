#CTI-110
#M5Lab2
#William Cox
#22 October 2017


import turtle
#Setting the screen color
turtle.bgcolor("black")
#this command changes the shape by default it is an arrow
turtle.shape("turtle")
#changes the spped the turtle draws 
turtle.speed(9)
#this is for the width of the drawing
turtle.pensize(10)

# This is for the letter W
turtle.color("red")
turtle.up()
turtle.goto(-120, 0)
turtle.down()
turtle.right(65)
turtle.forward(90)
turtle.left(140)
turtle.forward(60)
turtle.right(140)
turtle.forward(60)
turtle.left(130)
turtle.forward(90)

# This is for the letter M
turtle.color("white")    
turtle.up()
turtle.goto(10, -70)
turtle.down()
turtle.right(0)
turtle.forward(90)
turtle.right(140)
turtle.forward(60)
turtle.left(140)
turtle.forward(60)
turtle.right(130)
turtle.forward(90)

# This is for the letter C
turtle.color("blue")
turtle.fillcolor("black")
turtle.up()
turtle.left(65)
turtle.forward(70)
turtle.left(90)
turtle.forward(100)
turtle.down()
turtle.left(100)
turtle.circle(50, 180)
