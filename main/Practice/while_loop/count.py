# Write a Python program to count the number of digits in a number using a while loop
a=int(input("Enter a number:"))
count=0
while a>0:
    a//=10
    count+=1
print("count=",count)