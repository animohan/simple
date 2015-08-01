#Converting a collection into a set
L=[1,2,1,3,2,4,5]
print("#Printing list L:",L)
print("#Converting the collection to set")
print(set(L))
print(list(set(L)))
print(list(set(['yy','cc','aa','xx','dd','aa']))) 

#Find list difference
print("Difference Set([1,3,5,7])-set([1,2,4,5,6])")
print(set([1,3,5,7])-set([1,2,4,5,6]))

print("\nDifference set('abcdeg)-set('abdghij')")
print(set('abcdefg')-set('abdghij'))

print(set(dir(bytes))-set(dir(bytearray)))

print(set(dir(bytearray))-set(dir(bytes)))
