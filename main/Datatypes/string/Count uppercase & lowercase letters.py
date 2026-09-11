str1=input("Enter the string:")
print(str1)
print("Length:",len(str1))
upper=0
lower=0
count=0
for i in str1:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1

print("Upper",upper)
print("Lower",lower)