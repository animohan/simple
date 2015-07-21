print('\n#Declaring a list')
L_int=[1,2,3]
L_str=['alpha','beta','gamma']
print(L_int)
print(L_str)

print('\n#Accessing elements of the list')
print('first element of L_int')
print(L_int[0])
print('2nd element of L_str')
print(L_str[1])

print('\n Elements of list can be accessed by -ve index')
print('last element of L_int')
print(L_int[-1])
print('2nd to last element of L_str')
print(L_str[-2])

print('\n # Adding the end of the list')
print(L_int+[4,5,6])
print(L_str+['delta','zeta','theta'])

print('\n # List type can be mixed')
print(L_int)
print(L_int.append('Hello'))
print(L_int)
print(L_int.pop(3))
print(L_int.pop(0))

print('\n# list can be sorted')
L_int.append(1)
print(L_int)
L_int.sort()
print(L_int)
L_int.reverse()
print(L_int)

print(L_str)
L_str.sort()
print(L_str)
L_str.reverse()
print(L_str)
