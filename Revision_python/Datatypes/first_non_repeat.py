s="swiss"
print(s)
freq={}
for i in s:
    if i in freq:
        freq[i]=i
    else:
        freq[i]=1
for i in s:
    if freq[i]==1:
        print("First:",i)
        break