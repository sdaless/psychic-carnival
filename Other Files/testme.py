print("This program generates new usernames!\n")

firstname = input("Enter your first name: ")
lastname = input("Enter last name: ")

username = firstname[0] + "." + lastname[:7]

print("\nYour username will be: ", username)