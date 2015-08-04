#Lists
print("Simple list commands")
L=[]#Declaring an empty list
L=[123,'abc', 1.23,{}] #collection of items
print(L)
L=['bob', 40.0,['dev','mgr']] #Nested sublists
print(L)
L=list('spam') #list of iterable items
print(L)
L=list(range(-4,4)) #list of successive integers
print(L[2])
print(L[2:4])
print(len(L))
L1=[123,'abc', 1.23,{}]
print(L+L1)
print(L+[55,66,77])
J=[11,22,33]
print(J)
J=J+list("95")
print(J)

print(L*3) #bigger list; all elements for L are repeated
for x in L: print(x) #printing lists
print(3 in L) #membership
print(L)
L.append(4)
print(L)# append only takes one argument; note print(L.append(4)) does not work
L.extend([5,6,7])
print(L)
L.insert(2,345)
print(L)
print(L.index(5))
L.count(3) #counts number of occurences
print(L)

print("\n#Sorting")
L.sort()
print(L)
J=['ABD','aBe','abc']
J.sort()
print(J)
J.sort(key=str.lower) #Normalize everything to lower case and sort; print does not change to lower case
print(J)
J.sort(key=str.lower,reverse=True)
print(J)

L.reverse()
print(L)
K=L.copy()
print(K)
L.clear()
print(L)
print(K.pop(0))
print(K)
K.remove(0)
print(K)
del K[0]
print(K)
del K[0:2]
print(K)
K[0:2]=[]
print(K)
K[0]=3
print(K)
K[0:0]=[6,5,4] #insertion in the begning
print(K)

K[:0]=[2,2,2] #insertion in the begning
print(K)

K[len(K):]=[0,0,0] #insertion in the begning
print(K)
K[0:3]=[9,8,7] #Replacement
print(K)
L=[x**2 for x in range(5)]
print("\n",L)

for x in [1,2,3]:
	print(x,end='')
print("\n")
for x in [1,2,3]:
	print(x,end=' ')
print("\n")
for x in [1,2,3]:
	print(x,end='/')
print("\n")

res=[c*4 for c in 'SPAM']
print(res)
#similar to
res=[]
for c in 'SPAM':
	res.append(c*4)
print(res)
print("\n",list(map(ord,'spam')))

#Nested lists
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[0])
print(matrix[0][0])
print(matrix[:][0]) #bit strange, need to revisit
print(matrix[0][:]) 