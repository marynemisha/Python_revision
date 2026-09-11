n=int(input("Enter:"))
ch=65
for i in range(n,0,-1):
    for j in range(i):
        print(chr(ch),end=" ")
        ch+=1
    print()