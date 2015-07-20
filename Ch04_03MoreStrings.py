print('#Formatting string output with specific messages')
print('%s, eggs, and %s' %('spam','bacon'))

print('#Another way of formatting string output')
print('{0}, Horse, Hen and {1}'.format('snake','Eagle'))
print('{}, beta, gamma and {}'.format('alpha','delta'))
print('{}, beta, gamma and {}'.format('delta','alpha'))

print('\n')
print('#Appending to the string')
S='Spam'
print(S+'ming')
#print(S._add_('mister'))

print('\n')
print('Othter ways to code string')
k='A\nB\tC'
print(k)
print(len(k))
print(ord('\n'))
