try:
    n=int(input("Enter:"))
    result=100/n
except ValueError:
    print("Invalid input....")
except ZeroDivisionError:
    print("Division by zero....")
else:
    print("Result is:",result)
finally:
    print("Division completed....")

