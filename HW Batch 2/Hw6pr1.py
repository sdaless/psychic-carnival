# Part 1: Create a game menu
# Display options, select, and run
# After it executes, ask the user if they want to view the menu again, loop.

from turtle import *
import random

def menu():

	print("Hello! Choose your GAME!")
	print("a - Mirror, Cockroach, Laser")
	print("b - The Dating Equation")
	print("c - Turtle Art Showcase")
	print("x - Exit")

	game = input("Game choice: ")

	if game in 'Aa':
		mircoclas()

	elif game in 'Bb':
		dating()

	elif game in 'Cc':
		turtle()

	elif game in 'Xx':
		print("Adios, amigo.")

#Mirror, Cockroach, Laser
def mircoclas():

	player1 = input("Player 1, do you want mirror, cockroach or laser? ")
	computer = random.choice(['mirror', 'cockroach', 'laser'])

	print("The computer has", computer)

	if player1 == computer:
		print("It's a TIE... but there can only be one. REMATCH!")

	elif player1 == "mirror" and computer == "laser":
		print("Mirror DEFLECTS laser! Player 1 WINS!")

	elif player1 == "laser" and computer == "mirror":
		print("Mirror DEFLECTS laser! Computer WINS!")

	elif player1 == "cockroach" and computer == "mirror":
		print("Cockroach DIRTIES mirror! Computer WINS!")

	elif player1 == "mirror" and computer == "cockroach":
		print("Cockroach DIRTIES mirror! Player 1 WINS!")

	elif player1 == "cockroach" and computer == "laser":
		print("Laser INCINERATES cockroach TO ASHES! Computer WINS!")

	elif player1 == "laser" and computer == "cockroach":
		print("Laser INCINERATES cockroach TO ASHES! Player 1 WINS!")


#The Dating Equation
def dating():
	
	userAge = float(input("First things first. How old are you? "))

	if userAge < 18: 
		print("You are a child. Puberty might change a thing or two! Give it a few years.")

	else:
		userAtr = float(input("How attractive would you say you are, on a scale of 1-10? "))
		loversAtr = float(input("How attractive would you say the person you have the hots for is, on a scale of 1-10? "))

	if userAtr < (loversAtr + 2): 
		print("Oof. It looks like they might be out of your league, pal.")

	elif loversAtr == loversAtr:
		print("Perfect match... barely.")

	else:
		print("That could work.")
		print("But the fact that you have to do MATH to make sure of that is a little weird, isn't it?")

#Turtle Artwork Showcase
def turtle():

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


menu()