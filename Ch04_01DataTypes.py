# Simple data type

#number
print('#Number')
print('number data types');
print(25*25)
print('\n')

print('#Float data types')
print(1.5*1.39)
print('\n')

print('#Length of a number: 5000')
print(len(str(5000)))
print('\n')

#Math module has more functions
print('#Math module has more functions');
import random
print ('#Random number printing')
print(random.random())
print(random.choice([1,2,3,5]))
print('\n')

#simple string operation
print('#Simple String Operation')
print('#Length of string :- Spam')
S='spam'
print('#Printing value assigned to S')
print(S)
print('\n')

print('#Length of S is')
print(len(S))
#accessing elements of the string
print('#Access to elementes of string')
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
print('\n')
S='shrubbery'
print('#Printing the string')
print(S)
L=list(S)
print('\n')
print('#Printing the List')
print(L)
print('\n')

print('#Replacing h with c in Shrubbery')
L[1]='c'
print(L)
print('\n')

#now converting to a string
print('#Converting list back to string')
print("".join(L))
print('\n')

B=bytearray(b'spam')
print(B)
B.extend(b'eggs')
print(B)
B.decode()
print('\n')

print('#Finding subset of a string')
#Finding subset
S='Spam'
print(S.find('pa'))
print('#Replace pa in Spam with XYZ')
print(S.replace('pa', 'XYZ'))
print('\n')

line = 'aaa,bbb,ccccc,dd'
print(line.split(','))
print(S.upper())

