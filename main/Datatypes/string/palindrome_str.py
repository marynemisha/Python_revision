str1 = input("Enter a string: ")
print(str1)

rev = ""

for i in range(len(str1)-1, -1, -1):
    rev += str1[i]

if str1 == rev:
    print("Palindrome")
else:
    print("Not Palindrome")