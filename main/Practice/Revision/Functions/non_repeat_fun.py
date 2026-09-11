def character(str1):
    freq={}
    for i in str1:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for i in str1:
        if freq[i]==1:
            print("First non repeating element:",i)

character("banana")
