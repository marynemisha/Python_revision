l=list(map(int,input("Enter:").split()))
print(l)
l.sort()
for i in range(len(l)-1):
    if l[i+1]!=l[i]+1:
        print("Missing number:",l[i]+1)