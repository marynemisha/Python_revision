# Write a Python program to demonstrate all types of operators in Python
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

#Arithmetic operators
print("Arithmetic operators")
print("Sum:",a+b)
print("Difference:",a-b)
print("Multiply:",a*b)
print("Divide:",a/b)
print("Modulus:",a%b)
print("Floor division:",a//b)
print("Exponentation:",a**b)

#comparison operators
print("\nComparison operators")
print("Equal to:",a==b)
print("Not equal to:",a!=b)
print("Less than:",a<b)
print("Less than or equal to:",a<=b)
print("Greater than:",a>b)
print("Greater than or equal to:",a>=b)

#Assignment operators
print("\nAssignment operators")
x=20
print("Assign:",x)
x+=5
print("Sum equal to:",x)
x-=10
print("Difference:",x)
x*=3
print("Multiply:",x)
x/=5
print("Divide:",x)
x%=5
print("Modulus:",x)
x//=5
print("Floor division:",x)
x**=3
print("Exponentation:",x)

#Logical operators
print("\nLogical operators")
print(a>20 and a<10)
print(b>20 and b<30)
print(not a<20)

#Bitwise operators
print("\nBitwise operators")
num1=60          #00111100
num2=13          #00001100
print(num1&num2)
print(num1|num2)
print(num1^num2)
print(~num1)

#Membership operators
print("\nMembership operators")
name="python"
print('p' in name)
print('z' not in name)

#Identity operators
print("\nIdentity operators")
x=[1,2,3]
y=x
print(x is y)
print(x is not y)

