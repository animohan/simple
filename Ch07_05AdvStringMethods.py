#Changing strings:
S='spammy'
S=S[:3]+'xx'+S[5:]
print(S)

S='spammy'
print(S.replace('mm','xx'))


#Finding a fixed size string and replacing that
S="xxxxSPAMxxxxSPAMxxxx"
where=S.find('SPAM')
S=S[:where]+'Eggs'+S[(where+4):]
print(S)

S="xxxxSPAMxxxxSPAMxxxx"
print(S)
print(S.replace('SPAM','EGGS'))
print(S) #Note S value does not change
print(S.replace('SPAM','EGGS',1)) #only 1 value is changed

#changing the string in place.
S='Spammy'
L=list(S)
print(L)
L[3]='x'
L[4]='x'
print(L)
S="".join(L)
print(S)

#String methods for parsing text
line='aaa bbb ccc'
col1=line[0:3]
col3=line[8:0]
print(col1)
print(col3)

line="bob,hacker,40"
line.split(',')
line ="i'mSPAMaSPAMlumber"
print(line.split("SPAM"))

#other common string method in action
line='The knights who say Ni !\n'
print(line)
print(line.rstrip())
print(line.isalpha())
print(line.upper())
print(line.endswith('Ni!'))
print(line.startswith('The'))

#String formatting expressions
print('that is a %d %s bird !' %(1,'bird')) #%d=number, %s=everything matches
exclamation='Ni'
print('The knights who say %s!' %exclamation)
print('%d %s %g you' %(1,'love', 4.0))#%g for float

x=1.23456789
print("%e" %x) #exponent
print("%f" %x) #decimal
print("%g" %x) #choose format by number content
print("%-6.2f" %x)
print("%05.2f" %x)
print("%+6.1f" %x)

#Dictionary based formatting
print('%(qty)d more %(food)s' %{'qty':1, 'food':'fish'}) #note use of dictionaries

template='{0},{1} and {2}'
print(template.format('spam','ham','eggs'))

template='{motto},{pork} and {food}'
print(template.format(motto='spam',pork='ham',food='eggs'))

template='{motto},{0} and {food}'
print(template.format('ham',motto='spam',food='eggs'))

template='{},{} and {}'
template.format('spam','eggs','ham')