#Sara D'Alessandro
#Homework #6

import random 
from turtle import *

#PROBLEM 1:

def menu():

	print("| the GAME DIRECTORY |")

	print("Behold:")
	print("a - Lasers. Roaches. Mirrors.")
	print("b - the dating equation™")
	print("c - art 'better than da vinci'")
	print("Or you can just press 'X' and leave.  You could do that too.")

	game = input("Whatchu wanna do? ")

	if game == "a":
		lasermirror()

	if game == "b":
		dateq()

	if game == "c":
		turtle()

	if game == "X":
		print("I see how it is.  Bye.  Hmph.")

def cont():
	
	cont = input("Wanna go again? y/n: ")
	
	if cont == "y":
		menu()
	if cont == "n":
		print("Sigh, okay.  Peace out.")



def lasermirror():

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

	cont()



def dateq():

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

	cont()




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

	cont()

menu()

