str1="abcd"
str2="cdab"
if len(str1)==len(str2) and str2 in str1+str1:
    print("Rotation")
else:
    print("Not rotation")