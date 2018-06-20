# Name:  Sara D'Alessandro
# Hw2pr1.py
# STRING slicing and indexing challenges

h = 'harvey'
m = 'mudd'
c = 'college'

# Problem 1:  'hey'
Answer1 = h[0] + h[4:6]
print(Answer1, "\n")

# Problem 2: 'collude'
Answer2 = c[0:4] + m[1:3] + c[-1]
print(Answer2, "\n")

# Problem 3: 'arveyudd'
Answer3 = h[1:] + m[1:]
print(Answer3, "\n")

# Problem 4: 'hardeharharhar'
Answer4 = h[:3] + m[-1] + c[-1] + (h[:3]*3)
print(Answer4, "\n")

# Problem 5: 'legomyego'
Answer5 = c[3:6] + c[1] + m[0] + h[-1] + c[4:6] + c[1]
print(Answer5, "\n")

# Problem 6: 'clearcall'
Answer6 = c[0] + c[3:5] + h[1:3] + c[0] + h[1] + c[2:4]
print(Answer6, "\n")



# LIST slicing & Indexing
pi = [3,1,4,1,5,9]
e = [2,7,1]

# Problem 0 (example): [2,7,5,9]
Answer0 = e[0:2] + pi[-2:]
print(Answer0,"\n")

# Problem 7: [7,1]
Answer7 = e[1:]
print(Answer7,"\n")

# Problem 8: [9,1,1]
Answer8 = pi[-1:-6:-2]
print(Answer8,"\n")

# Problem 9: [1,4,1,5,9]
Answer9 = pi[1:]
print(Answer9,"\n")

# Problem 10: [1,2,3,4,5]
Answer10 = e[-1:-4:-2] + pi[0:5:2]
print(Answer10)



