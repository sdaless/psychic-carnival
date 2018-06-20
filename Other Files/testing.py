#import turtle

#kate = turtle.Pen()
#jake = turtle.Pen()
#lisa = turtle.Pen()

#kate.forward(50)

#jake.penup()
#jake.goto(100,100)
#jake.pendown()
#jake.forward(80)

#lisa.penup()
#lisa.goto(300,300)
#lisa.pendown()
#lisa.forward(25)

#turtle.mainloop()

#Create Instances
rob = Employee()
craig = Employee()
lisa = Customer()

rob.name = "Robert Domanski"
rob.job_title = "Professor"
rob.salary = "Not enough"

print("Employee #1:", rob.name, rob.job_title, rob.salary)

choice = input(":Do you want to change their salary: ")

if choice == 'y':
	rob.setSalary()
else:
	print("Alrighty then...")

print("Employee #1's current salary is:", rob.salary)

