l=list(map(int,input("Enter the list:").split()))
print("Length of list:",len(l))
result=0
n=len(l)+1
total=n*(n+1)//2
result=total-sum(l)
print("Missing number:",result)