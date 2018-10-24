
# simple if statment. Shows indentation rules
a=10
b=20
if a>b:
	print(a)
else:
	print(b)


#simple combination of while and if statements
while True:
	reply = input('Enter Text:')
	if reply == 'stop': break
	print(reply.upper())


#Like Math: Another example with if and while

while True:
	reply= input("Enter number; 0 to stop")
	if(reply) == '0': break
	print(int(reply)**2)

print("Bye")