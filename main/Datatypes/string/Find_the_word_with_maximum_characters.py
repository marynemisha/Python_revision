str1="I Love programming"
print(str1)
max=""
word=""
for i in str1:
    if i!=" ":
        word+=i
    else:
        if len(word)>len(max):
            max=word
        word=" "
if len(word)>len(max):
    max=word

print("Max:",max)
