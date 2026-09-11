#frequency of each character without using a dictionary.
str1="banana"
freq=""
for i in str1:
    if i not in freq:
        freq+=i
        print(i,"=",str1.count(i))