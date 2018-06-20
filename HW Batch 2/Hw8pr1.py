# Name: Arianna Chinchilla
# File name: Hw8pr1.py

import math

def gcd(x,y):
	"""
	return greatest common divisor of x and y
	"""
	if x%y == 0:
		return y
	return gcd(y, x%y)

print("Welcome!")
print("This program will use Euclid's Algorithm to determine the perfect number of tiles for your floors.")
x = int(input("Enter the 'x' dimensions of the rectangle area: "))
y = int(input("Enter the 'y' dimensions of the rectangle: "))
print(gcd(x,y),"tiles should be used.")