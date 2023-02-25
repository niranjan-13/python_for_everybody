'''
Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split() method.
The program should build a list of words. For each word on each line check
to see if the word is already in the list and if not append it to the list.
When the program completes, sort and print the resulting words in python 
sort() order as shown in the desired output. 
'''
fname = input("Enter file name: ")
fname = "romeo.txt"
read = open(fname)
new = list()
out=[]
for text in read:
    text = text.rstrip()
    new = text.split()
    for i in new:
        out.append(i)
romeo=[]
for word in out:
    if word not in romeo:
        romeo.append(word)
romeo.sort()
print(romeo)
