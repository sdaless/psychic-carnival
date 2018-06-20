import random

print("Welcome to the Roulette Table!")
wallet = 500
numWins = 0
numLosses = 0
numSpins = 0

startingBetAmt = int(input("How much do you want to bet? $"))

currentBetAmt = startingBetAmt

# Spin the wheel 10,000 times

while numSpins < 10000 and wallet > 0:

	result = random.choice(['black','red'])

	if result == 'red':
		wallet = wallet + currentBetAmt
		currentBetAmt = startingBetAmt
		numWins = numWins + 1

	elif result == 'black':
		wallet = wallet - currentBetAmt
		currentBetAmt = currentBetAmt * 2
		numLosses = numLosses + 1

	numSpins = numSpins + 1

print("Total money after", numSpins, "spins is $", wallet)
print("Number of wins: ", numWins)
print("Number of losses: ", numLosses)



