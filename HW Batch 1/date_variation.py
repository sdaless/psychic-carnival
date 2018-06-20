# The Dating Equation Variation
# Variable here determines compatibility between the user and the user's crush via how "attractive" they are

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