def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
        return True
n=int(input("Enter the number:"))
if prime(n):
    print("Prime")
else:
    print("Not prime")


