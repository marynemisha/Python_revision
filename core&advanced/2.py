s="banana"
print(s)
print(len(s))
freq={}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for key,value in freq.items():
    print(key,":",value)