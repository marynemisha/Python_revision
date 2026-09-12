s="aaabbcdd"
freq=""
for i in s:
    if i not in freq:
        freq+=i
print("Non repeat:",freq)