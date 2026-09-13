d={"a":10,"b":20,"c":5}
highest=max(d.values())
for i in d:
    if d[i]==highest:
        print("Key:",i)