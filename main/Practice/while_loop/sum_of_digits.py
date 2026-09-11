# Write a Python program to find the sum of digits of a number using a while loop
num=int(input("Enter the number:"))
sum=0
while(num>0):
    digits=num%10
    num//=10
    sum+=digits
print("sum=",sum)