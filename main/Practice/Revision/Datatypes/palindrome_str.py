s=input("Enter the string:")
rev=""
for i in s:
    rev=i+rev
if s==rev:
    print("palindrome")
else:
    print("Not palindrome")