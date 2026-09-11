s="Python 3"
print("String:",s)
vowels=0
consonants=0
digits=0
spaces=0
for i in s:
    if i in 'aeiouAEIOU':
        vowels+=1
    elif i.isdigit():
        digits+=1
    elif i.isspace():
        spaces+=1
    else:
        consonants+=1

print("Vowels:",vowels)
print("Consonants:",consonants)
print("Digits:",digits)
print("Spaces:",spaces)
