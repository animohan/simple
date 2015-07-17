# Simple data type

#number
print('number data types');
print(25*25)

print('float data types')
print(1.5*1.39)

print('lenght of a number: 5000')
print(len(str(5000)))

#Math module has more functions
import random
print ('Random number printing')
print(random.random())
print(random.choice([1,2,3,5]))

#simple string operation
print('length of string :- Spam')
S='spam'
print(S)
print(len(S))
#accessing elements of the string
print(S[0])
print(S[1])
print(S[-1])
#any expression can be used in brackets
print(S[1:3])
print(S+'_eating contest')

#Strings are immutable objects and their values cannot be changed after creatin
#uncomment and run the nextline to see the error
#S[0]='z' 

#but can run expression to make new pbjec
S='z'+S[1:]
print(S)

#you can change text based data in place if you either expand it into a list of individual
#character and join it back

S='shrubbery'
L=list(S)
print(S)
print(L)

L[1]='c'
print(L)

#now converting to a string
print("".join(L))

B=bytearray(b'spam')
print(B)
B.extend(b'eggs')
print(B)
