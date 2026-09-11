s="banana"
max_count=0
max_char=""
for i in s:
    c=s.count(i)
    if c > max_count:
        max_count=c
        max_char=i
print("Most highest:",max_char)
