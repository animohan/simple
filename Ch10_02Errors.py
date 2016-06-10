S='123'
T='xxx'

#function isdigit confirms if the input is a number
S.isdigit() 
T.isdigit()

#Now a program using it
while True:
	reply = input("Enter a number; Enter 0 to stop: ")
	if reply == '0': break
	elif not reply.isdigit():
		 print("Try numbers")
	else:
		print(int(reply)**2)
print('Bye')

#Handling errors with try statments
# code first runs try part and if there are no exceptions then run the else
#more in later chapters
while True:
	reply = input('Enter text; Enter stop to exit')
	if reply == 'stop': break
	try:
		num = int(reply)
	except:
		print('Try entering a number')
	else:
		print(num**2)

print("Bye")

#Note that try can be used to intercept any error and one does not need to run
# line by line error check. The above code will fail trying a float. Here is a 
# code that takes care of any errors

while True:
	reply = input("Enter number; Enter 0 to exit")
	if reply == '0':break
	try:
		print(int(reply)**2)
	except:
		print("Try again with integers")

print("Bye")


#Nesting code 3 levele deep

while True:
	reply = input ("Enter text; enter stop to exit: ")
	if reply == 'stop': 
		break
	elif not reply.isdigit():
		print("Try again with integers ")
	else:
		num = int(reply)
		if num<20:
			print("low number ")
		else:
			print("high number ")
print("Bye")
