#Sara D'Alessandro
#Homework #7

from turtle import *

def circle():
    center = (20, 100)
    for i in range(360):
    	forward(i + 1)
    	right(i + 1)
    circle = Circle(centre, 20)

circle()
exitonclick()