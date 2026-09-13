s = "hello world hello python"
d={}
word=""
for i in s:
    if i!=" ":
        word+=i
    else:
        if word in d:
            d[word]+=1
        else:
            d[word]=1
        word=""
if word in d:
    d[word]+=1
else:
    d[word]=1
print(d)