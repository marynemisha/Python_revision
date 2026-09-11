l=input("Enter:")
print("List:",l)
freq={}
for i in l:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for key,value in freq.items():
    print(key,":",value)

