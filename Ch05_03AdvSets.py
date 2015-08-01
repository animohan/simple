#Converting a collection into a set
L=[1,2,1,3,2,4,5]
print("#Printing list L:",L)
print("#Converting the collection to set")
print(set(L))
print("Note: Converting to set removes duplicate elements")
print("\n#Converting from a collection to set to a list")
print(list(set(L)))
print(list(set(['yy','cc','aa','xx','dd','aa']))) 

#Find list difference
print("Difference Set([1,3,5,7])-set([1,2,4,5,6])")
print(set([1,3,5,7])-set([1,2,4,5,6]))

print("\nDifference set('abcdeg)-set('abdghij')")
print(set('abcdefg')-set('abdghij'))

print(set(dir(bytes))-set(dir(bytearray)))

print(set(dir(bytearray))-set(dir(bytes)))

#Sets can be used for order neutral tests
L1,L2=[1,2,3,4,5],[5,4,3,2,1]
print("\nConsider two collections:L1=[5,4,3,2,1]; L2=[1,2,3,4,5]; Comparing them")
print(L1==L2)
print("Now convert them to sets and compare them")
print(set(L1)==set(L2))