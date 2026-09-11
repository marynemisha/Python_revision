s=input("Enter the string:")
print("String:",s)
freq={}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i in s:
    if freq[i]==1:
        print("First Non repeating character:",i)
        break