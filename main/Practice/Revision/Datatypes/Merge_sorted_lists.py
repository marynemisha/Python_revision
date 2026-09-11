l1=list(map(int,input("Enter the first list:").split()))
l2=list(map(int,input("Enter the second list:").split()))
l3=l1+l2
l3.sort()
print("Merge sorted lists:",l3)