from turtle import *

penup()
goto(0,0)
pendown()
color("red")
width(20)

while True:	
	left(45)
	forward(100)
	if abs(pos()) < 1:
		break

penup()
goto(-50,-20)
pendown()
color("gray")
width(40)
right(90)
forward(200)


penup()
goto(-110,160)
color("red")
width(5)
right(90)
pendown()
forward(30)
left(90)
forward(30)
left(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)


penup()
goto(-95,160)
pendown()
backward(40)
forward(20)
left(90)
forward(80)

penup()
goto(-40,160)
pendown()
forward(80)
left(90)
forward(30)
left(90)
forward(80)
left(90)
forward(30)

penup()
goto(40,160)
pendown()
forward(30)
left(90)
forward(80)
penup()
right(180)
forward(60)
pendown()
right(90)
forward(30)
left(90)
forward(20)


done()
