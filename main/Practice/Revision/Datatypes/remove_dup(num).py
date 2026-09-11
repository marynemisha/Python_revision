num=input("Enter the number:")
result=""
for i in num:
    if i not in result:
        result+=i
print(result)