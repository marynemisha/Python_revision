str1 = input("Enter a string: ")
print("str1:",str1)
freq = ""
for i in str1:
    if i not in freq:
        count = 0
        for ch in str1:
            if i == ch:
                count += 1
    print(i, "=", count)
    freq += i