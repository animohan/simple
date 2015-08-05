#Dictionaries
print("\n#Dictionaries")
D={'spam':2,'ham':1,'eggs':3}
print(D)
print(D['spam'])
print('Length of D:',len(D))
print("Test for existence: ham in D:", 'ham' in D)
print("Keys of D:",list(D.keys()),"\n",D.keys())

print("\n#Changing Dictionary values")
print("Old D:",D)
D['ham']=['grill','bake','fry']
print("New D:", D)
del D['eggs']
print("Delete a key:eggs.D=",D)
D['brunch']='Bacon'
print("Add a key 'brunch':=",D)

print("\n#More Dictionary methods")
print("List D keys", list(D.keys()))
print("List D items", list(D.items()))

print("fetching a key, when it exists:",D.get('spam'))
print("fetching a key, when it does not exist:",D.get('june'))
print("fetching a new item by putting its value",D.get('toast',88))
print(" above statement does not change D:-",D)

print("\n#Dictionary update methods")
print("D:",D)
D2={'toast':4,'muffin':5}
print("D2:",D2)
D.update(D2)
print("D.update(D2) gives:",D)
print("Popping value, deletes the key:",D.pop('toast'), D.pop('muffin'))
print("D:",D)

print("\n#An aside, pop a list")
L=['aa','bb','cc','dd']
print("L:",L)
print("L.pop():",L.pop())
print("L.pop(1):",L.pop(1))

print("\n#Example of Movie database using Dictionaries")
table={'1975':'Holy Grail',
	'1979':'Life of Brian',
	'1983':'The meaning of Life'}

year='1983'
print("Table:", table)
print("Movie of year 1983:",table[year])
print("\nFor loop in Dictionary")
for year in table:
	print(year + '\t' + table[year])
print("\n")

for year in table:
	print(year,'\t',table[year])

print("\n#Different mapping for same dictionary")

table={'Holy Grail':'1975',
	'Life of Brian':'1979',
	'The meaning of Life':'1983'}
print("Table key:",table.keys())
print("Table items:", table.items())
print("\n")

#Compreshensions in action for dictionaries
print([title for (title, year) in table.items() if year=='1975'])

K='Holy Grail'
print(table[K])
V='1975'
print([key for (key,value) in table.items() if value==V])
print([key for key in table.keys() if table[key]==V])
