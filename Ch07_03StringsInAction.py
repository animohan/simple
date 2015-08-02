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