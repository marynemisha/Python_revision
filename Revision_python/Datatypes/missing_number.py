list=[1,2,3,4,6]
print(list)
n=len(list)+1
total=n*(n+1)//2
sum=0
for i in list:
    sum+=i
missing=total-sum
print("Missing:",missing)