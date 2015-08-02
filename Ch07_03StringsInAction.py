#Some basic operations
print(len('abc'))
print('abc'+'def')
print('Nil'*4)
print("-"*30)

#Iterating over string
myjob="hacker"

for c in myjob:
	print(c)

for c in myjob:
	print(c, end='') #look at the difference on terminating the string with null

print("\n")

#Finding substring
print("k" in myjob)
print("z" in myjob)
print("hack" in "hacker")

#Indexing and slicing
print("\n #Indexing and Slicing")
S='Spam'
print(S)
print(S[0],S[3])
print(S[-4],S[-1])
print(S[0-len(S)],S[len(S)-1])
print(S[1:])
print(S[:3])
print(S[0:3:2])
S='0123456789'
print(S[0:10:2])
print(S[0:10:3])
print(S[::2])
print(S[::-1])
print(S[::-2])
print(S[0:10:-1]) #print nothing, bounds are not reversed
print(S[10:0:-1])

print(S[2:7:1])
print(S[7:2:-1]) #Note reversing the start and end point and step sign does not give, reverse of string

#String conversions
print("\n#String Conversions")
S='42'
print(int(S)+42)

K=23
print(str(K)+" Wolves")

#Character Code conversions
print("\n#Character code conversions")
#converting character to its ASCII values
print(ord('s'))
print(chr(115))
print(chr(ord('s')+1)) #print next value after s
print(ord('5')-ord('0'))

print("\nUsing the character code conversions to convert from binary")
B='1101'
I=0
while B!="":
	I=I*2+(ord(B[0])-ord('0'))
	B=B[1:]

print(I)

print(int('101',2))
print(int('101',3))
print(bin(5))

print("\nChanging Strings")
S='Spam'
# S[0]='x' #causes an error, string object does not support item assignment
S=S+'Spam!'
print(S)
S=S[:4]+'Burger'+S[-1]
print(S)
S=S[0]
print(S)
S="Hello World"
S=S.replace("World","Human")
print(S)

print("That is a %d %s bird !" %(1,'flying'))
