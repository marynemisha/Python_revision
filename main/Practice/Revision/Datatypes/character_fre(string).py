s=input("Enter the string:")
print("String:",s)
freq=""
for i in s:
    if i not in freq:
        freq+=i
        print(i,"=",s.count(i))