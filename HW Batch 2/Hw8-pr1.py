#Sara D'Alessandro
#Homework #8

from math import *

print("Hi, welcome to the | Euclidean Algorithm |! To ensure an accurate answer, please make sure your dimensions are the same unit!")

x = int(input("What are the x dimensions of your rectangle? " ))
y = int(input("What are the y dimensions of your rectangle? "))

#Example:
#x = 210, y = 45
#Divide 210 by 45, get result 4 with remainder 30, so 210 = 4 x 45 + 30
#Divide 45 by 30, get result 1 with remainder 15, so 45 = 1 x 30 + 15
#Divide 30 by 15, get result 2 with remainder 0, so 30 = 2 x 15 + 0
#Greatest common divison or 210 and 45 is 15

def euclid(x, y):
	if x % y == 0:
		return y
	return euclid(y, x % y)

print("You should use", euclid(x, y), "tiles.")

	#if x < y:
		#return x % y 
		#while  
		#as long as the remainder is greater than 0...


