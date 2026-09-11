#repeated
s="Programming"
rep=""
for i in s:
    if i in rep:
        print("Repeated element:",i)
        break
    else:
        rep+=i

