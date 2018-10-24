class Person:
	def __init__(self, name, job=None, pay=0):
		self.name=name
		self.job=job
		self.pay=pay

	def lastName(self):
		return self.name.split()[-1]

	def giveRaise(self,percent):
		self.pay=int(self.pay+percent*self.pay)

	def __repr__(self):
		return '[Person: %s, %s]' %(self.name,self.pay)


#defining subclasses
class Manager(Person):
	def __init__(self, name, pay):
		Person.__init__(self,name,'mgr',pay)

	def giveRaise(self, percent, bonus=0.10):
		Person.giveRaise(self, percent+bonus)

class Department:
	def __init__(self,*args):
		self.members=list(args)


	def addMember(self, person):
		self.members.append(person)


	def showAll(self):
		for person in self.members:
			print(person)

	def giveRaises(self, percent):
		for person in self.members:
			person.giveRaise(percent)

if __name__=='__main__':
	#self-test code
	bob = Person('Bob Smith')
	sue = Person('Sue Jones', job='dev', pay=100000)
	print(bob.name, bob.pay)
	print(sue.name, sue.pay)
	print("Bob's lname:", bob.lastName(), "Sue's lname:",sue.lastName())
	sue.giveRaise(0.1)
	print("Sue's pay after raise:", sue.pay)
	print(sue)
	tom = Manager ('Tom Jones',50000)
	tom.giveRaise(0.10) #Runs the manager version of giveRaise
	print(tom.lastName()) #runs inherited method
	print(tom)

	print('---All Three---')
	for obj in (bob,sue,tom):
		obj.giveRaise(.10)
		print(obj)


	development=Department(bob,sue)
	development.addMember(tom)
	development.giveRaises(0.10)
	development.showAll()