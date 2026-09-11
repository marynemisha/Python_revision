#total and avg of a string

str1 = "123abc456"
total=0
avg=0
count=0
for i in str1:
    if i.isdigit():
        total+=int(i)
        count+=1
avg=total/count
print("Total:",total)
print("Avg:",avg)
