#Sara D'Alessandro
#Homework #3

import random

#PROBLEM 1:
sum1 = 0
for i in range (101):
    sum1 = sum1 + i

print(sum1)

sum2 = 0
for i in range (101):
    if i % 2 == 0:
        sum2 += i

print(sum2)

sum3 = 0
for i in range (100):
    if i % 2 == 1:
        sum3 += i

print(sum3)



#PROBLEM 2:
def dna_to_rna(x):
    
    base = ["A","C","G","T"]
    rnabase = ["U","G","C","A"]
    
    print("RNA sequence will be: ", end="")

    for i in x:
        if i == 'A': 
            print(rnabase[0], end="")
        elif i == 'C':
            print(rnabase[1], end="")
        elif i == 'G':
            print(rnabase[2], end="")
        elif i == 'T':
            print(rnabase[3], end="")
        else:
            pass

    cont()

def cont():

    cont = input("Enter another DNA sequence or enter 'X' to quit: ")
    if cont == 'X':
        print("Peace out my dude.")
    else:
        dna_to_rna(cont)
            
print("Welcome to the DNA to RNA Nucleotide Converter-er.")            
dna = input("Enter DNA sequence: ")

dna_to_rna(dna)



#PROBLEM 3:

import random
import math

x1 = random.randint(0,30)
y1 = random.randint(0,30)

def menu():

	x = 15
	y = 15

	print("Welcome to the Hunt, you doomed, ill-fated soul.")
	command = input("Enter a direction, such as 'N', 'S', 'E', 'W', or enter 'X' to flee (exit): ")

	if command in 'Nn':
		y = y + 1
		result(x,y)
	elif command in 'Ss':
		y = y - 1
		result(x,y)
	elif command in 'Ee':
		x = x + 1
		result(x,y)
	elif command in 'Ww':
		x = x - 1
		result(x,y)
	elif command in 'Xx':
		print("We await your return, Hunter.")
	else:
		print("You have been foiled, Hunter.  Try again... if you dare.")


def result(x,y):

	distance = round(math.sqrt((x-x1)*(x-x1)+(y-y1)*(y-y1)))

	if distance == 0:
		print("Well played.  Against all odds, you found the secret treasure.")

	if distance > 0:
		print("You are", distance, "spaces away from the sunken secret place.")
		print("Your current coordinates are",x,y,".")
		command = input("Enter a direction such as 'N', 'S', 'E', 'W', or 'X' to exit: ")

		if command in 'Nn':
			y = y + 1
			result(x,y)
		elif command in 'Ss':
			y = y - 1
			result(x,y)
		elif command in 'Ee':
			x = x + 1
			result(x,y)
		elif command in 'Ww':
			x = x - 1
			result(x,y)
		elif command in 'Xx':
			print("We await your return, Hunter.")

menu()

