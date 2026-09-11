s="python"
for i in range(len(s),0,-1):
    for j in range(i):
        print(s[j],end=" ")
    print()