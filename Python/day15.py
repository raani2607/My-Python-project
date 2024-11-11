try:
    number1 = int(input("Enter first number :"))
    number2 = int(input("Enter your second : "))
    result = number1 / number2
    print(result)
except ZeroDivisionError:
    print("do not divide by zero")
except ValueError as e:
    print("divide only numbers in the input:", e)
    # else is not a must in the syntax
# else:
#     print(result)

finally:
    print("end of code")

