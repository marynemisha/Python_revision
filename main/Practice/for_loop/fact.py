# Write a Python program to find the factorial of a number using a for loop
a=int(input("Enter the number:"))
fact=1
for i in range(1,a+1):
    fact*=i
print("Factorial=",fact)