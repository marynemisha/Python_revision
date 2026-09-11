s="python"
for i in range(len(s)):
    for j in range(i+1):
        print(s[len(s)-1-j],end=" ")
    print()