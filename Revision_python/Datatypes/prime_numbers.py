n=7
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("Prime")
else:
    print("Not prime")


# list of numbers
# list = [2, 3, 4, 5, 6, 7, 8, 9, 11]
# for n in list:
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#        print(n)