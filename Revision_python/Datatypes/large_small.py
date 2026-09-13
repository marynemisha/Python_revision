list = [10, 5, 20, 3, 15]
largest=list[0]
smallest=list[0]
for i in list:
    if i>largest:
        largest=i
    if  i< smallest:
        smallest=i
print("Largest:",largest)
print("Smallest:",smallest)