# The Dating Equation

userAge = float(input("How old are you? "))
loversAge = float(input("How old is the person you have the hots for? "))

if userAge < 18: 
	print("You are a child. You shouldn't date anyone that isn't also a minor!")

else:
	creepyFactor = (userAge - 7) * 2

	if loversAge > creepyFactor: 
		print("UNACCEPTABLE T H O T")

	elif loversAge == creepyFactor:
		print("Perfect match... but just barely.")

	else:
		print("Okay, that could work.")
		print("But the fact that you have to do MATH to make sure of that...")
		print("is more than a little dubious. Better sign a prenup.")