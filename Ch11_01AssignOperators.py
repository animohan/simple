#simple assignment operators:
nudge=1
wink=2
print("Nudge = %d , Wink = %d " %(nudge,wink))
A, B = nudge, wink # equivalent to A=nudge, B=wink
[C,D]=[nudge, wink] #list assignment

#simple swap
nudge,wink=wink, nudge

# This works because python creates a temporary tuple that saves original values
# of the variables on the right while the statement run

#Tuple and list assignment in Python are generalized to accept any type of 
#sequence that is iterable and has same length as sequence on left
[a,b,c]=[1,2,3]
[u,v,w]='ABC'
print("u = %s , v = %s, w = %s " %(u,v,w))