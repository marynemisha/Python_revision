d1 = {"a": 10, "b": 20}
d2 = {"b": 30, "c": 40}
d1.update(d2)
print(d1)



for keys in d2:
    if keys in d1:
        d1[keys]+=d2[keys]
    else:
        d1[keys]=d2[keys]
print(d1)
