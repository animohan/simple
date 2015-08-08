class Person:
	def __init__(self, name, job=None, pay=0):
		self.name=name
		self.job=job
		self.pay=pay

	def lastname(self):
		return self.name.split()[-1]

	def giveRaise(self,percent):
		self.pay=int(self.pay+percent*self.pay)

if __name__=='__main__':
	#self-test code
	bob = Person('Bob Smith')
	sue = Person('Sue Jones', job='dev', pay=100000)
	print(bob.name, bob.pay)
	print(sue.name, sue.pay)
	print("Bob's lname:", bob.lastname(), "Sue's lname:",sue.lastname())
	sue.giveRaise(0.1)
	print("Sue's pay after raise:", sue.pay)