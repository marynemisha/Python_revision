# Find the second most frequent character in a string.
s="abbccc"
freq={}
for i in s:
    freq[i]=s.count(i)
x=sorted(freq.values(),reverse=True)
for i in freq:
    if freq[i]==x[1]:
        print("second:",i)
        break