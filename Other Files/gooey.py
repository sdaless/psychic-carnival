from graphics import *

win = GraphWin("What Roleplaying Hero Are You?", 500, 500)

win.setBackground("red")

t = Text(Point(250, 100), "Welcome to 'What Hero Are You?' Click anywhere to start!")
t.setSize(25)
t.draw(win)

win.getMouse() 

e = Entry(Point(250, 200), 15)
e.draw(win)

m = win.getMouse()
user_choice = e.getText()
if user_choice == "Mario":
	user_choice = "Mario"
elif user_choice == "Peach":
	user_choice = "Peach"
elif user_choice == "Bowser":
	user_choice = "Bowser"
else:
	user_choice = "Bowser"

t.undraw()
e.undraw()


# Show what the user chose
imm = Image(Point(250, 250), "mario.gif")
imp = Image(Point(250, 250), "peach.gif")
imb = Image(Point(250, 250), "bowser.gif")

t2 = Text(Point(250, 100), "You chose: ", user_choice)
t2.setSize(25)

if user_choice == "Mario":
	imm.draw(win)
	win.setBackground("salmon")
elif user_choice == "Peach":
	imp.draw(win)
	win.setBackground("pink")
elif user_choice == "Bowser":
	imb.draw(win)
	win.setBackground("purple")

t2.draw(win)
t3 = Text(Point(250, 450), "Click to play against computer!")
t3.draw(win)

win.getMouse()

# Flip the coin!
imm.undraw()
imp.undraw()
imb.undraw()
t2.undraw()
ch = random.choice(["Mario", "Peach", "Bowser"])
t3.undraw()

t4 = Text(Point(250, 450), "It's a TIE!")
t4.setSize(25)
t5 = Text(Point(250, 450), "You WIN!")
t5.setSize(25)
t6 = Text(Point(250, 100), "Mario defeated Bowser!")
t7 = Text(Point(250, 100), "Peach charmed Mario!")
t8 = Text(Point(250, 100), "Bowser kidnapped Peach!")
t9 = Text(Point(250, 450), "You LOSE!")
t9.setSize(25)

if ch == user_choice:
	t10 = Text(Point(250, 100), "Computer chose: " ch)
	t4.draw(win)
elif ch == "Mario" and user_choice == "Peach":
	t7.draw(win)
	t5.draw(win)
elif ch == "Peach" and user_choice == "Mario":
	t7.draw(win)
	t9.draw(win)
elif ch == "Bowser" and user_choice == "Mario":
	t6.draw(win)
	t5.draw(win)
elif ch == "Mario" and user_choice == "Bowser":
	t6.draw(win)
	t9.draw(win)
elif ch == "Peach" and user_choice == "Bowser":
	t8.draw(win)
	t5.draw(win)
elif ch == "Bowser" and user_choice == "Peach":
	t8.draw(win)
	t9.draw(win)
else:
	t9.draw(win)

if ch == "Mario":
	imm.draw(win)
elif ch == "Peach":
	imp.draw(win)
else:
	imb.draw(win)




win.getMouse()
win.close()