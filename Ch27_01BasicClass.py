class FirstClass:
	def setdata(self,value):
		self.data=value

	def display(self):
		print(self.data)

x=FirstClass()
y=FirstClass()

x.setdata("King Arthur")
y.setdata(3.14159)

x.display()
y.display()

x.anothername="spam" #can attach a completely new attribute

print(x.anothername)

class SecondClass(FirstClass):
	def display(self):
		print('Current value ="%s"' %self.data)


z=SecondClass()
z.setdata(42)
z.display()

class ThirdClass(SecondClass):
	def __init__(self,value):
		self.data=value
	def __add__(self, other):
		return ThirdClass(self.data+other)
	def __str__(self):
		return '[ThirdClass: %s]' %self.data
	def mul(self,other):
		self.data*=other

a=ThirdClass('abc')
a.display()
print(a)

b=a+'xyz'
b.display()
print(b)

a.mul(3)
print(a)

#Classes can be empty
class rec: pass
rec.name='Bob'
rec.age=40
print(rec.name)
x=rec()
y=rec()
print(x.name, y.name)
x.name='Sue'
print(rec.name, x.name, y.name)
print(list(rec.__dict__.keys()))
print((x.__dict__.keys())) # name was explicity set for x, hence it show up
print((y.__dict__.keys())) # name was inheritied from class, so it doesn show up
print(x.__class__) #link to the class,
print(rec.__bases__) #clases are derived, so to access their superclass

#methods that are normally created by def inside a class, can be created indpendenty
def uppername(obj):
	return obj.name.upper()

rec.method=uppername

print(x.method())

#comparing dicitionaries and classes. 

#Tuple based record
rec1=('Bob',40.5,['dev','mgr']) 
print("Tuple Name:",rec1[0])

#dictionary based record
rec2={}
rec2['name']='Bob'
rec2['age']=40.5
rec2['jobs']=['dev','mgr']
print("Dictionary name:",rec2['name'])

class rec3: pass
rec3.name='Bob'
rec3.age=40.5
rec3.jobs=['dev','mgr']

print("Class/Object:", rec3.name)

#Proper full blow class

class Person:
	def __init__(self, name, jobs, age=None):
		self.name=name
		self.jobs=jobs
		self.age=age
	def info(self):
		return(self.name, self.jobs)

rec4=Person('Bob',['dev','mgr'],40.5)
rec5=Person("Sue",['dev','cto'])

print(rec4.jobs)
print(rec5.info())
