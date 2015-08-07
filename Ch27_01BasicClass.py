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
print((x.__dict__.keys()))
