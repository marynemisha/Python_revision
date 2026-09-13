num=121
temp=num
rev=0
while num>0:
    digits=num%10
    rev=rev*10+digits
    num//=10
if temp==rev:
    print("Palindrome")
else:
    print("Not palindrome")