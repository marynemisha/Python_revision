# d1={"a":20,"b":40}
# d2={"c":60,"d":80}
# d1.update(d2)
# print(d1)

#without update()
d1={"a":20,"b":40}
d2={"c":60,"d":80}
d3={}
for i in d1:
    d3[i]=d1[i]
for i in d2:
    d3[i]=d2[i]
print(d3)