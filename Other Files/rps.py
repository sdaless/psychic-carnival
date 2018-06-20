import random

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


