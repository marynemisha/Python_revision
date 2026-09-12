a=[10,2,30,29,18]
large=a[0]
for i in a:
    if i>large:
        large=i
print("Largest:",large)
second_large=a[0]
for i in a:
    if i>second_large and i!=large:
        second_large=i
print("Second largest:",second_large)

small=a[0]
for i in a:
    if i<small:
        small=i
print("Smallest:",small)

second_small=a[0]
for i in a:
    if i<second_small and i!=small:
        second_small=i
print("Second smallest:",second_small)


#using sort()
print("................Using sort()..................")
a.sort()
print("Smallest:",a[0])
print("Second smallest:",a[1])
print("Largest:",a[-1])
print("Second largest:",a[-2])