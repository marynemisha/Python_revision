s1={1,2,3}
s2={2,3,4}
result=set()
for i in s1:
    if i in s2:
        result.add(i)
print(result)
