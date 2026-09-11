n=4
num=10
for i in range(n,0,-1):
    for j in range(i):
        print(num,end=" ")
        num-=1
    print()