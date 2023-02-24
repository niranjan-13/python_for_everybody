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
