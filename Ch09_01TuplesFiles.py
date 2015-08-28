#Tuple are like dictionaries but not mutable

print("Tuple Concat (1,2)+(3,4)=", (1,2)+(3,4))
print("Tuple Repeat (1,2)*4=", (1,2)*4)
T=(1,2,3,4)
print("Tuple T=",T)
print("Indexing T[0]=", T[0])
print("Indexing T[:3]=",T[0:3])

T=('cc','aa','dd','bb')
tmp =list(T)
tmp.sort()
print("Sorted T", T)
print("Another way to sort", sorted(T))

#List comprehension to convert tuples
T=(1,2,3,4,5)
L=[x+20 for x in T]
print(L)
print("T.index(2)=",T.index(2)) #index of occurence
print("T.count(2)=",T.count(2)) #number of elemented with value=2

#Lists being immutable only works at the top level.
T=(1,[2,3],4)
#T[1]='spam' #throws an error
T[1][0]="spam"
print(T)


#Files
myfile=open('myfile.txt','w')
myfile.write('Hello Text file \n')
print(myfile.write('goodbye text file \n'))
myfile.close()

myfile=open('myfile.txt')
print(myfile.readline())
print(myfile.readline()) #for reading second line
print(myfile.readline()) # for reading third line

open('myfile.txt').read()
print(open('myfile.txt').read()) #reads the entire line into a string

for line in open('myfile.txt'):
	print(line)

#binary file
#data=open('data.bin','rb').read() #need binary file
#print(data)