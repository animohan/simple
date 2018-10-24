print("Dictionaries to simulate flexible lists")
L=[]
#L[99]='spam' # will have a failure

D={}
D[99]='spam'
print(D)

#Note integers are used as strings
table={1975:"Holy Grail",
		1979:"Life of Brian",
		1983:"The meaning of Life"}

print(table)

print("\n#Using dictionaries for sparse data structures: Tuple keys")
Matrix={}
Matrix[(2,3,4)]=88
Matrix[(7,8,9)]=99
X=2;Y=3;Z=4
print(Matrix[(X,Y,Z)])
print(Matrix)

#if matrix is accessed with non existent key, it will throw an error; Here is a fix

if(2,3,6) in Matrix:
    print(Matrix[(2,3,6)])
else:
    print(0)

#other option
try:
    print(Matrix[(2,3,4)])
except KeyError:
    print(0)

print(Matrix.get((2,3,4),0))
print(Matrix.get((2,3,6),0))
