#String Methods
S="A Beautiful Mind"
print(S.capitalize())
print(S.casefold())
print(S.center(50,'a'))
print(S.count('Bea',0,25))
print(S.encode('utf','strict'))
print(S.endswith('ind',0,20))
S1="A Beautiful\tMind"
print(S1.expandtabs(10))
print(S.find('ful',0,20))
S2="A Beautiful Mind's number {0}"
print(S2.format(41+2))
S2="A Beautiful Mind's numbers are {0},{1}"
print(S2.format(42,24))
print(S.index('ful',0,20))
S4=25
print(S.isalpha())
#print(S4.isalpha())
print("isalnum:",S.isalnum())
#print(S4.isalnum())
print("isdigit:", S.isdigit())
#print(S4.isdigit())
print("isidentifier:",S.isidentifier())
print("islower:",S.islower())
print("isprintable", S.isprintable())
print("isnumeric",S.isnumeric())
print("isspace:",S.isspace())
print("istitle:",S.istitle())
print("isupper:",S.isupper())
print("isjoin",S.())
