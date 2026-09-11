def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    print("Factorial:",f)
n = int(input("Enter the number:"))
fact(n)