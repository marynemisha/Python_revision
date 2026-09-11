s="Python"
print("String:",s)
print("Length:",len(s))
freq=""
for i in s:
    if i not in freq:
        print(i,"=",s.count(i))
        freq+=i