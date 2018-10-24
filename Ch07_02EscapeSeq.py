#Escape Sequences
print("\nHello World") #Newline character
print("\\n Hello World") #print backslash
print("\'Hello World") #print quotes
print("\"Hello World") #print double quotes
print("\a Hello World") #Outputs a sound.

print("Hello\bWorld") #backspace; notice how it removes 'o'
print("Hello World \f") #form feed
print("Hello \r World") #carriage returm

print("Hello \t World") #Horizontal tab
print("Hello \v World") #vertical tab
print("Hello World \xBD") #print hex value BD
print("Hello World \051") #print octal value
print("Hello World \0") #print null value
# print("Hello World \N{25}") #Unicode database ID
#print("Hello World", \u0123) #unicdode character with 16 bit hex value
#print("Hello World \U01230123") #unicode character with 32 bit hex value
#print("Hello World \other") #Not an escape(keeps both \ and other)
