#String operations
print("\n#Basic string type")
S='' #Empty string
print(S)
S="Spam's" #Double quote same as single
print(S)
print('s\np\ta\x00m') # Escape sequences
S="""......mutlipline.....""" #Triple quoted block string
print(S)
S=r'\temp\spam' #Rawstrings(no escapes)
print(S)
B=b'sp\xc4m' # Byte strings; Does not seem to work
print(B)
U=u'sp\u00c4m' #Unicode strings
print(U)
S1="Event"
S2="Horizon"
print("String concatenation: ",S1+S2)
print("String multiplication ", S1*3)
S1=S2[2]
print("Index:", S1)
S1=S2[2:]
print("Slicing",S1)
print("length of a string", len(S2)) #length of the string
print("a %s parrot" %('kind')) #String formatting
print("a {0} parrot " .format('dumb')) #another string formatting
print(S2.find('ri')) # Index of ri in Horizon
print(S2.find('rz'))