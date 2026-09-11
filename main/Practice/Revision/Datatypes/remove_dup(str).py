s=input("Enter the string:")
result=""
for i in s:
    if i not in result:
        result+=i
print(result)