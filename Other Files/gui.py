from graphics import*

win = GraphWin("Some Basic GUI Examples",700,500)
win.setBackground("yellow")

# Create two points
apoint = Point(45, 80)
anotherpoint = Point(500, 300)
apoint.draw(win)
anotherpoint.draw(win)

# Create a line between the two points
myline = Line(apoint, anotherpoint)
myline.setArrow("last") # options: first, last, both, none


# Display the user's input
win.getMouse()
userinput = textbox1.getText()
mylabel.undraw()
label2 = Text(Point(450, 80), "Welcome, " + userinput)
label2.setStyle("bold italic")
label2.setTextColor("red")
label2.draw(win)



win.getMouse() # pause for click in window

win.close()