# l = list(map(int, input("Enter list elements: ").split()))
# l.sort()
# print("Second Smallest:", l[1])
# print("Second Largest:", l[-2])

#duplicate removing with same question
l=list(map(int,input("Enter the list:").split()))
l=list(set(l))
print(l)
l.sort()
print("Smallest:",l[1])
print("Largest:",l[-2])
