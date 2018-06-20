# Example of Recursion (calculating factorials)

def factorial(num):

	# Set the base case (stopping point)

	if num == 1:

		return 1

	# Make the function call itself with a smaller number

	else: 

		return num * factorial(num - 1)


print(factorial(5))
print(factorial(25))