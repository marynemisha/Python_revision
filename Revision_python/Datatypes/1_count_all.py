# vowels, consonants, digits, spaces and special characters in a string.
s="Hello 123!"
print("string:",s)
vowels=0
consonants=0
digits=0
spaces=0
special=0
for i in s:
    if i in 'aeiouAEIOU':
        vowels+=1
    elif i.isalpha():
        consonants+=1
    elif i.isdigit():
        digits+=1
    elif i.isspace():
        spaces+=1
    else:
        special+=1

print("Vowels:",vowels)
print("consonants:",consonants)
print("digits:",digits)
print("spaces:",spaces)
print("special:",special)