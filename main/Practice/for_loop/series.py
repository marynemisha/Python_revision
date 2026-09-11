# Write a Python program to print Fibonacci series
a=0
b=1
limit=int(input("Enter the limit:"))
for i in range(limit):
    print(a)
    c=a+b
    a=b
    b=c
