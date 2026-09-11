str1 = input("Enter a sentence: ")
print("str1:",str1)
word = ""
first=""
for i in str1 :
    if i != " ":
        word += i
    else:
        if word != "":
            i = word[0]
            if i in "AEIOUaeiou":
                print(word)
        word = ""