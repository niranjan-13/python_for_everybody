#Finding repeated words in a sample textbook using dictionary
name = 'text_book.txt'
mydict = {}
with open(name) as fhand:
	for line in fhand:
		words = line.split()
		for word in words:
			mydict[word]=mydict.get(word,0)+1
	for i in mydict.keys():
		print(i,mydict[i])
print("The Most repeated word is:")
maxWord = None
maxTimes = 0
for i,j in mydict.items():
	if j>maxTimes:
		maxTimes = j
		maxWord = i
	
print("Most repeated word is :",maxWord)
print("It is repeated ",maxTimes,"times")
