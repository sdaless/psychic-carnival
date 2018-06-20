import random

numHeads = 0
numTails = 0
wallet = 5
betAmt = float(input("How much do you want to bet? "))

for i in range (100):

	coin = random.choice(['heads','tails'])

	print("The result is: ", coin)

	if (coin == 'heads'):
		numHeads = numHeads + 1

	else:
		numTails = numTails + 1	

print("Number of Heads: ", numHeads)
print("Number of Tails: ", numTails)
print("Money in your wallet NOW: ")

	#print("Hello world!", end='')
