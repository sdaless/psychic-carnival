# Convert date format from xx/xx/xxxx to "October 23, 1999"

dateStr = input("Enter a date in number format: ")

# Split the string into 3 new strings
monthStr, dayStr, yearStr = dateStr.split("/")