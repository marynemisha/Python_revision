# Write a Python program to check whether a number is prime or not
lower=int(input("Enter lower limit:"))
upper=int(input("Enter upper limit:"))
for num in range(lower,upper+1):
    if num>1:
        for j in range(2,num):
            if num%j==0:
                break
        else:
            print(num)




