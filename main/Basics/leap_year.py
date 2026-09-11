# Write a Python program to check whether a given year is a leap year or not using if-else
year=int(input("Enter the year:"))

if year % 400 == 0:
    print(year,"is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")



#{ working:
# year=2024
#  if 2024%400==0:                             #false
# elif 2024%4==0 and 2024%100!=0:
#       #true          #true                   #true
#
#   2024--->leap year}




# 400-ൽ divide ചെയ്താൽ → Leap Year
#
# അല്ലെങ്കിൽ
#
# 4-ൽ divide ചെയ്യുകയും
# 100-ൽ divide ആകരുത് → Leap Year
#
# അല്ലെങ്കിൽ → Not Leap Year