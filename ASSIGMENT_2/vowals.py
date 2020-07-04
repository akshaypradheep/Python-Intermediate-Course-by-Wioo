vowals=['A','E','I','O','U']
j=0
a=str(input("Enter the alphabet :")).upper()
for i in vowals:
	if i==a:
		j=1
		pass
	pass
if j==1:
	print ("The Letter is vowal")
else:
	print ("The Letter isn't vowal")
	pass