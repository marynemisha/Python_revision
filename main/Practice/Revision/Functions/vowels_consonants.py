def string1(str1):
    v=0
    c=0
    print("Length of string:",len(str1))
    for i in str1:
        if i.lower() in 'aeiou':
            v+=1
        else:
            c+=1
    print("vowels:",v)
    print("consonants:",c)
string1("Python Djnago@full stack")
