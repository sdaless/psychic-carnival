# import the freaking library
from appJar import gui

# create a GUI variable called app
app = gui("Character Archetype Quiz", "600x400")
app.setResizable(canResize=False)
app.setBg("light blue")
app.setFont(18)
font = "Courier"
app.setLocation("CENTER")

# add & configure widgets - widgets get a name, to help reference later

app.addLabel("title", "What Character Archetype are you?")
username = app.addLabelEntry("Welcome! Enter your name: ")
app.addLabel("subtitle", "Click one of the buttons below to continue!")
app.setLabelBg("title", "light green")

# welcome
app.addTextArea("Welcome",username,".")

# add homescreen images
app.setImageLocation("Image Folder")

app.addImage("mage", "mage2.gif")

# This stuff
a = 0
b = 0
c = 0
d = 0
e = 0

def tally(x):
	if x == "A":
		global a
		a += 1
		return a
	if x == "B":
		global b
		b += 1
		return b
	if x == "C":
		global c
		c += 1
		return c
	if x == "D":
		global d
		d += 1
		return d
	if x == "E":
		global e
		e += 1
		return e

# buttons
app.addButtons(["Start Quiz", "Exit"], press)

app.startPagedWindow()
app.startPage()
app.addLabel("Q1: If you were caught in a position to defend yourself, which weapon would you prefer?")
app.addLabel("A: Sword")
app.addLabel("B: Wand (assuming you could cast spells)")
app.addLabel("C: Fists")
app.addLabel("D: Daggers")
app.addLabel("E: Peace and love, man")
answer1 = input("Choose one: ")
tally(answer1)
app.stopPage()

app.startPage()
app.addLabel("l21", "Label 2")
app.stopPage()

app.startPage()
app.addLabel("l3", "Label 3")
app.stopPage()

app.startPage()
app.addLabel("l4", "Label 4")
app.stopPage()
app.stopPagedWindow()

def press(button):
	if button == "Start Quiz":
		# start quiz


	else: 
		app.stop()


		app.startPage()
		app.addLabel("l3", "If you were a superhero, who would you be?")
		app.addEmptyMessage("cc")
		app.addEmptyMessage("dd")
		app.addRadioButton("choice3", "Superman")
		app.addRadioButton("choice3", "Doctor Strange")
		app.addRadioButton("choice3", "Wonderwoman")
		app.addRadioButton("choice3", "Batman")
		app.addRadioButton("choice3", "Aquaman")

		
		app.stopPage()




		app.startPage()
		app.addLabel("l4", "If you were a supervillain, who would you be?")
		app.addEmptyMessage("ee")
		app.addEmptyMessage("ff")
		app.addRadioButton("choice4", "Two-Face")
		app.addRadioButton("choice4", "Riddler")
		app.addRadioButton("choice4", "Bane")
		app.addRadioButton("choice4", "Catwoman")
		app.addRadioButton("choice4", "Poison Ivy")

				
		app.stopPage()




		app.startPage()
		app.addLabel("l5", "What mythical creature would you be?")
		app.addEmptyMessage("gg")
		app.addEmptyMessage("hh")
		app.addRadioButton("choice5", "Centaur")
		app.addRadioButton("choice5", "Elf")
		app.addRadioButton("choice5", "Ogre")
		app.addRadioButton("choice5", "Basilisk")
		app.addRadioButton("choice5", "Angel")
		
		
		app.stopPage()




		app.startPage()
		app.addLabel("l6", "Which personality trait best describes you?")
		app.addEmptyMessage("ii")
		app.addEmptyMessage("jj")
		app.addRadioButton("choice6", "Courageous")
		app.addRadioButton("choice6", "Wise")
		app.addRadioButton("choice6", "Powerful")
		app.addRadioButton("choice6", "Cunning")
		app.addRadioButton("choice6", "Compassionate")
		
		
		app.stopPage()




		app.startPage()
		app.addLabel("l7", "Which of the following seems to be a recurring") 
		app.addLabel("l77", "problem for you?")
		app.addEmptyMessage("kk")
		app.addEmptyMessage("ll")
		app.addRadioButton("choice7", "I tend to see things in black-and-white,") 
		app.addLabel("l077", "good-or-bad.")
		app.addRadioButton("choice7", "I tend to overanalyze situations.")
		app.addRadioButton("choice7", "I tend to lose my temper too quickly.")
		app.addRadioButton("choice7", "I tend to be sadistic.")
		app.addRadioButton("choice7", "I tend to have my kindness taken for") 
		app.addLabel("granted.")
		
		
		app.stopPage()




		app.startPage()
		app.addLabel("l8", "What role do you see yourself playing in an action") 
		app.addLabel("l88", "movie?")
		app.addEmptyMessage("mm")
		app.addEmptyMessage("nn")
		app.addRadioButton("choice8", "The Hero")
		app.addRadioButton("choice8", "The Sidekick")
		app.addRadioButton("choice8", "The Rival")
		app.addRadioButton("choice8", "The Anti-hero")
		app.addRadioButton("choice8", "The Group Mom")
		
	
		app.stopPage()




		app.startPage()
		app.addLabel("l9", "Which occupation below would you choose?")
		app.addEmptyMessage("oo")
		app.addEmptyMessage("pp")
		app.addRadioButton("choice9", "Lawyer")
		app.addRadioButton("choice9", "College professor")
		app.addRadioButton("choice9", "Professional Boxer")
		app.addRadioButton("choice9", "Mercenary")
		app.addRadioButton("choice9", "EMT worker")
		
	
		app.stopPage()




		app.startPage()
		app.addLabel("l10", "Which book/series is your favorite out of the") 
		app.addLabel("l110", "following?")
		app.addEmptyMessage("qq")
		app.addEmptyMessage("rr")
		app.addRadioButton("choice10", "Divergent")
		app.addRadioButton("choice10", "Harry Potter")
		app.addRadioButton("choice10", "Sun Tzu's Art of War")
		app.addRadioButton("choice10", "V for Vendetta")
		app.addRadioButton("choice10", "The Giving Tree")
		
		
		app.stopPage()




		app.startPage()
		app.addLabel("l11", "Pick a virtue out of the following (shoutout 2") 
		app.addLabel("l111", "whoever gets the reference):")
		app.addEmptyMessage("ss")
		app.addEmptyMessage("tt")
		app.addRadioButton("choice11", "Candor")
		app.addRadioButton("choice11", "Erudite")
		app.addRadioButton("choice11", "Abegnation")
		app.addRadioButton("choice11", "Dauntless")
		app.addRadioButton("choice11", "Amity")
		
	
		app.stopPage()



print("Q2: How do you tend to handle conflicts?")
print("A: Speak my mind and use force only if need be.")
print("B: Cast brujería on my enemies.")
print("C: Fight them. No one wants to catch these hands.")
print("D: Secretly plot their demise. They better sleep with one eye open.")
print("E: I am a tender soul that cannot handle conflict.")
answer2 = input("Choose one: ")
tally(answer2)

print("Q3: If you were a superhero, who would you be?")
print("A: Superman")
print("B: Doctor Strange")
print("C: Wonderwoman")
print("D: Batman")
print("E: Aquaman")
answer3 = input("Choose one: ")
tally(answer3)

print("Q4: If you were a supervillain, who would you be?")
print("A: Two-Face")
print("B: Riddler")
print("C: Bane")
print("D: Catwoman")
print("E: Poison Ivy")
answer4 = input("Choose one: ")
tally(answer4)

print("Q5: What mythical creature would you be?")
print("A: Centaur")
print("B: Elf")
print("C: Ogre")
print("D: Basilisk")
print("E: Angel")
answer5 = input("Choose one: ")
tally(answer5)

print("Q6: Which personality trait best describes you?")
print("A: Courageous")
print("B: Wise")
print("C: Powerful")
print("D: Cunning")
print("E: Compassionate")
answer6 = input("Choose one: ")
tally(answer6)

print("Q7: Which of the following seems to be a recurring problem for you?")
print("A: I tend to see things in black-and-white, good-or-bad.")
print("B: I tend to overanalyze situations.")
print("C: I tend to lose my temper too quickly.")
print("D: I tend to be sadistic.")
print("E: I tend to have my kindness taken for granted.")
answer7 = input("Choose one: ")
tally(answer7)

print("Q8: What role do you see yourself playing in an action movie?")
print("A: The Hero")
print("B: The Sidekick")
print("C: The Rival")
print("D: The Anti-hero")
print("E: The Group Mom")
answer8 = input("Choose one: ")
tally(answer8)

print("Q9: Which occupation below would you choose?")
print("A: Police officer")
print("B: College professor")
print("C: Professional Boxer")
print("D: Mercenary")
print("E: EMT worker")
answer9 = input("Choose one: ")
tally(answer9)

print("Q10: Which book/series is your favorite out of the following?")
print("A: Divergent")
print("B: Harry Potter")
print("C: Sun Tzu's Art of War")
print("D: V for Vendetta")
print("E: The Giving Tree")
answer10 = input("Choose one: ")
tally(answer10)

print("Q11: Pick a virtue out of the following (shoutout 2 whoever gets the reference):")
print("A: Candor")
print("B: Erudite")
print("C: Abnegation")
print("D: Dauntless")
print("E: Amity")
answer11 = input("Choose one: ")
tally(answer11)

def result():
	if a > b and a > c and a > d and a > e:
		print("You are a Knight!")
	elif b > a and b > c and b > d and b > e:
		print("You are a Mage!")
	elif c > a and c > b and c > d and c > e:
		print("You are a Tank!")
	elif d > a and d > b and d > c and d > e:
		print("You are an Assassin!")
	elif e > a and e > b and e > c and e > d:
		print("You are a Healer!")
	else:
		print("You're 2 complicated. Please take quiz again and change like one of your answers.")

result()

# start the bloody GUI
app.go()
