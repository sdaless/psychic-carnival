#Sara D'Alessandro
#Homework #10

from graphics import *
import random

win = GraphWin("The Dating Equation!", 600, 400)
win.setBackground("light blue")

t = Text(Point(300, 100), "Welcome to the Dating Equation! Enter Your Age!")
t.setSize(25)
t.draw(win)

e = Entry(Point(300, 300), 30)
e.draw(win)

m = win.getMouse()

userAge = (e.getText())
float(input(userAge))

e.undraw()
t.undraw()

if userAge < 18:
	t2 = Text(Point(300, 100), "You are a child.  Puberty might change a thing or two! Give it a few years.")
	t2.setSize(15)
	t2.draw(win)
	win.getMouse()
	win.close()

else:
	e2 = Entry(Point(300, 200), 15)
	e2.draw(win)
	t3 = Text(Point(300, 100), "How attractive would you say you are, on a scale of 1-10?")
	t3.draw(win)
	e3 = Entry(Point(300, 90), 15)
	e3.draw(win)
	t4 = Text(Point(300, 100), "How attractive would you say the person you have the hots for is, on a scale of 1-10?")
	t4.draw(win)
	userAtr = (e2.getText())
	float(input((userAtr)))
	loversAtr = (e3.getText())
	float(input((loversAtr)))
	

	if userAtr < (loversAtr - 2):
		e2.undraw()
		e3.undraw()
		t3.undraw()
		t4.undraw()
		t5 = Text(Point(300, 200), 15, "Oof. It looks like they might be out of your league, pal.")
		t5.draw(win)
		win.getMouse()
		win.close()

	elif userAtr == loversAtr:
		t6 = Text(Point(300, 200), 15, "Perfect match... barely.")
		t6.draw(win)
		win.getMouse()
		win.close()

	else: 
		t7 = Text(Point(300, 200), 15, "That could work. But the fact that you have to do MATH to make sure of that is a little weird, isn't it?") 
		t7.draw(win)
		win.getMouse()
		win.close()



#if userAge < 18: 
	#print("You are a child. Puberty might change a thing or two! Give it a few years.")

#else:
	#userAtr = float(input("How attractive would you say you are, on a scale of 1-10? "))
	#loversAtr = float(input("How attractive would you say the person you have the hots for is, on a scale of 1-10? "))

	#if userAtr < (loversAtr + 2): 
		#print("Oof. It looks like they might be out of your league, pal.")

	#elif loversAtr == loversAtr:
		#print("Perfect match... barely.")

	#else:
		#print("That could work.")
		#print("But the fact that you have to do MATH to make sure of that is a little weird, isn't it?")



