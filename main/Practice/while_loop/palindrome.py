# Write a Python program to check whether a number is a palindrome or not
num=int(input("Enter the number:"))
temp=num
rev=0
while num>0:
    digits=num%10
    num//=10
    rev=rev*10+digits
if temp==rev:
    print(temp,"palindrome number...")
else:
    print(temp,"Not a palindrome number...")