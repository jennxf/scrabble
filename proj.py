import sys

f = open("sowpods.txt", "r")

words = [] # creates an empty list called words

for line in f:
    line = line.strip()
    words.append(line)

f.close()

#this is a test

scores = {"A": 1, "C": 3, "B": 3, "E": 1, "D": 2, "G": 2,
         "F": 4, "I": 1, "H": 4, "K": 5, "J": 8, "M": 3,
         "L": 1, "O": 1, "N": 1, "Q": 10, "P": 3, "S": 1,
         "R": 1, "U": 1, "T": 1, "W": 4, "V": 4, "Y": 4,
         "X": 8, "Z": 10}


if len(sys.argv)==2:
	rack=sys.argv[1].strip()
else:
	print "Please input rack after proj.py <your_rack>"
	exit()


valid_words=set()
for word in words:
	for letter in word:
		if letter in rack:
			valid_words.add(word)

score1=[]
for word in valid_words:
	count=0
	for letter in word:
		count+=scores[letter]

	a=(count,word)
	score1.append(a)

b = sorted(score1, key=lambda tup: tup[0])
for item in b[::-1]:
	print str(item[0]) +" "+ item[1]









