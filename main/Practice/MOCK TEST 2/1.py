#palindrome string
s=input("Enter the string:")
rev=""
for i in s:
        rev=i+rev
if s==rev:
    print("Palindrome")
else:
    print("Not palindrome")