s="aabbcdd"
freq=""
longest=""
for i in s:
    if i not in freq:
        freq+=i
if len(freq)>len(longest):
    longest=freq

print("Non repeat:",freq)
print("Longest:",longest)