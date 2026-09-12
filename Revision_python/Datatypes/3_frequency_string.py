# Find the frequency of each character in a string.
s="programming"
freq=""
for i in s:
    if i not in freq:
        print(i,"=",s.count(i))
        freq+=i