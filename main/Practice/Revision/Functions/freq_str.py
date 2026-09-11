def frequency(str1):
    freq=""
    for i in str1:
        if i not in freq:
            freq+=i
            print(i,"=",str1.count(i))
frequency("banana")