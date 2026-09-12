# Reverse each word in a sentence without changing the order of the words.
s="Hello world python"
word=""
for i in s:
    if i!=" ":
        word=i+word
    else:
        print(word,end=" ")
        word=""
print(word)


#s="Hello world python"
# result=""
# for i in s:
#     result=i+result            #o/p :nohtyP dlroW olleH
# print(result)