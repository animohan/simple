#Chapter talks about how references work.
print("Reference same integer")
a=35
print("a=", a)
b=a
print("Set b=a")
a=70
print("Changed value of a=70")
print("a=",a)
print("b=",b)
print("Though b was set equal to a(b=a), changing value of a did not change value of b")
print("Changing a=a+2:a=")
a=a+2
print(a)
print("Value of b:",b)

print("\n#Trying the assignment with Arrays/Lists")
L1=[2,3,4]
L2=L1
L3=L1[:]
print("Assigned following values L1=[2,3,4]; L2=L1;L3=L1[:]")
print("L1:",L1)
print("L2:",L2)
print("L3:",L3)
print("Now setting L1[0]=24")
L1[0]=24
print("L1:",L1)
print("L2:",L2)
print("L3:",L3)
print("L3 creates a copy of the original L1 instead of just referencing it")

print("\n#Taking a look at equality")
print("Assigned following values L=[2,3,4]; M=L")
L=[2,3,4]
M=L
print("L:",L)
print("M:",M)
print("L==M?",L==M)
print("L is M: i.e are they referencing same object?", L is M)
print("\nNow declaring M=[2,3,4], same as L")
M=[2,3,4]
print("L==M?",L==M)
print("L is M: i.e are they referencing same object?", L is M)
print("Result was false, though L and M are same arrays, they are referencing different objects")

print("\nAssigned following values b=2; b=a")
a=2
b=a
print("a:",a)
print("b:",b)
print("a==b?",a==b)
print("a is b: i.e are they referencing same object?", a is b)
