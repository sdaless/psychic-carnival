print("A Day At Hunter College: A Choose Your Own Adventure Experience")
print("Wow! Hunter College! Aren't you excited to be here, on your first day? What do you wanna do first?")

print("a) Go to the third floor via elevator and check out the cafeteria.")
choice1 = input("b) Take a peek into the USG office. ")

if choice1 == 'a': 
	print("Oh fiddlesticks! The elevator isn't working.") 
	print("Or maybe it's being held up? Either way, you wait around a good ten minutes before you decide you're better off just taking the stairs.") 
	print("Good thing your class doesn't start for another hour. Being late on your first day would suck. The only problem now is that all those stairs made you sweaty and thirsty.")
	
	print("a) Go get something to drink from the vending machine.") 
	choice2a = input("b) Rinse off your b.o. in the bathroom. ")
	if choice2a == 'a': 
		print("You approach a vending machine, absolutely parched.  You really could go for a bottle of your favorite effervescent beverage right about now.")  
		print("How do you proceed?")

		choice3a = input("a) Bang on the glass and loudly demand the infernal machine dispense your beverage of choice.")
		if choice3a == 'a':
			print("The machine stands there stoically.  It doesn't comply with your request.  It mocks you with its indifferent silence, and succumbing to both madness and dehydration, you fall into unconsciousness.")
			print("Maybe you can bother with school another day. END.")

	if choice2a == 'b':
		print("You approach a gray door with a restroom sign.  You push past the door... into the back of a waiting student.  Well.  It seems like there's a line; all the stalls and all the sinks are being used.")
		print("Immediately you feel the pressure and stress of deciding between waiting for a stall or finding another bathroom overwhelm you.  The real world is too intense.  You are confronted with all of your life decisions in this bathroom.")
		print("In the throes of an existential crisis, you decide you can't handle the undue stress of college and decide to go home. END.")


if choice1 == 'b': 
	print("Ah, the USG (Undergraduate Student Government) office! A sign on the door SAYS they're offering free tea and coffee...")
	print("But no one is here.  It's empty and barren, much unlike Hunter's hallways.  I guess no one cares about USG-- why should you?")
	print("You are overcome with apathy.  It must be the air of the USG office.  You feel such disdain for USG's empty promises that you turn towards the exit and walk out of your first day of class. END.")



# a) > Go to the third floor via elevator and check out the cafeteria.
# b) Take a peek into the USG office

	# 1a - Oh fiddlesticks! The elevator isn't working. 
	# Or maybe it's being held up? Either way, you wait around a good ten minutes before you decide you're better off just taking the stairs. 
	# Good thing your class doesn't start for another hour. Being late on your first day would suck. The only problem now is that all those stairs made you sweaty and thirsty. 

		# a) > Go get something to drink from the vending machine.
		# b) Rinse off your b.o. in the bathroom.

			# 2a - You approach the vending machine, absolutely parched.  You really could go for a bottle of your favorite effervescent beverage right about now.  
			# How do you proceed?

				# a) > Bang on the glass and loudly demand the infernal machine dispense your beverage of choice.
				# b) Put money into the machine like a normal person.

					# 3a - The machine stands there stoically.  It doesn't comply with your request.  It mocks you with its indifferent silence.

						# a) Give up and go to class.
						# b) Go to the bathroom?




