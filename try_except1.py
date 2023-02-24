#Converting String to Integer Using try and except 
val = input("Enter:")
try:
	new_val=int(val)
except:
	new_val=-1
if(new_val == -1):
	print("You Entered Incorrect String, Try agian!")
else:
	print("You entered :")
	print(new_val)
