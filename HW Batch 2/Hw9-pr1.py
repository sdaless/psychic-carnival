#Sara D'Alessandro
#Homework #9

count = 0
count1 = 0
wordcount = 0
trump = 0
clinton = 0
infile = open("DebateTranscript.txt", "r")
searchString = input("Enter a search term for your transcript: ")
interruptions = "..."

for line in infile:

	if searchString in line:
		count += 1

	if "TRUMP:" in line:
		trump += 1

	if "CLINTON:" in line:
		clinton += 1

	if interruptions in line:
		count1 += 1

if trump > clinton:
	result = trump
	name = "Trump"

else:
	result = clinton
	name = "Clinton"

print(name,"spoke the most:", result, "times.")
print("The word", searchString, "appears", count, "times in the text.")
print("There were", count1, "interruptions in the transcript.")

infile.close()