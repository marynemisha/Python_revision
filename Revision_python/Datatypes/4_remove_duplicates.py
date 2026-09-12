# Remove duplicate characters from a string while preserving the first occurrence.
s="programming"
freq=""
for i in s:
    if i not in freq:
        freq+=i
print(freq)