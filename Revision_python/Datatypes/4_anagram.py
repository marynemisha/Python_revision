#Check whether two strings are anagrams or not.
str1="listen"
str2="silent"
print("Str1:",str1)
print("str2:",str2)
print("Length of str1:",len(str1))
print("Length of str2:",len(str2))
if len(str1)!=len(str2):
    print("Not anagram")
else:
    count=0
for ch in str1:
    c1=0
    c2=0
    for i in str1:
        if i ==ch:
            c1+=1
    for j in str2:
        if j==ch:
            c2+=1
    if c1==c2:
        count+=1
if count==len(str1):
    print("Anagram")
else:
    print("Not anagram")