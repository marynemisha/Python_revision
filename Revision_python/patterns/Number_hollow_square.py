n=3
num=1
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print(num,end=" ")
            num+=1
        else:
            print(" ",end=" ")
    print()