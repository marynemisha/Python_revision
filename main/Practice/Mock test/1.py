#non-repeated character
s="aabbcddee"
freq={}
for i in s:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for i in s:
    if freq[i]==1:
        print("Non Repeating elements:",i)
        break


# s="programming"
# freq={}
# for i in s:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for i in s:
#     if freq[i]==1:
#         print("Non repeating elements:",i)
#         break