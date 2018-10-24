#Declaring sets
x=set('abcde')
y=set('bdxyz')
print("Set x:")
print(x)
print("Set y:")
print(y)

print("Difference of set x-y:")
print(x-y)
print("\nUnion of sets x|y:")
print(x|y)
print("\nIntersection of sets x&y:")
print(x&y)
print("\nXOR of sets x^y:")
print(x^y)
print("\nx is a subset of y: x<y")
print(x<y)
print("\nx is a superset of y: x>y")
print(x>y)
print("\nMembership in a set, is 'e' in c")
print('e' in x)


#Additionally, set object provides methods that correspond to these operations.

print("\nIntersection of sets x&y:")
z=x.intersection(y)
print("z=x.intersection(y)=",z)


print("\nInsert an item:")
z.add('SPAM')
print("z.add('SPAM'):",z)

z.update(set(['X','Y']))
print("\nMerging, in place Union:z.update(set['X','Y']):",z)

z.update(set('uv'))
print(z)

z.remove('b')
print("\nRemoving element from set: z.remove('b'):",z)


#sets can be used as containers for iterating variable
print("#Sets can be used as containers for iterating variable")
for item in set('abc'):
	print(item*3)

print('#Set expressions can often work with any iterable type like lists')
S=set([1,2,3])
print("Set S:",S)
# print("S|[3,4]",S|[3,4]) : Marking as expression as this is an error
print("S|[3,4]:",S|set([3,4])) 

print("\n#Methods take any literal type")
S.union([3,4])
print("S.union([3,4]):",S.union([3,4]))

print("\n#New way for declaring sets")
u={1,2,3,4}
v={3,4,5,6}
print("Set u:")
print(u)
print("Set v:")
print(v)

print("Difference of set u-v:")
print(u-v)
print("\nUnion of sets u|v:")
print(u|v)
print("\nIntersection of sets u&v:")
print(u&v)
print("\nXOR of sets u^v:")
print(u^v)
print("\nu is a subset of v: u<v")
print(u<v)
print("\nu is a superset of v: u>v")
print(u>v)
print("\nMembership in a set, is 'e' in u")
print('e' in u)






