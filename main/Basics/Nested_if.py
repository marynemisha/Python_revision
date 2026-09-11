# Write a Python program to find the largest of three numbers using nested if
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>b:
    if a>c:
        print(a,"is largest")
    else:
        print(c,"is largest")
else:
    if b>c:
        print(b,"is largest")
    else:
        print(c,"is largest")