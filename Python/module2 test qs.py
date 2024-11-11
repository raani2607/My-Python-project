# #calculate the area of a rectangle
# length = int(input("What is the length of the rectangle :"))
# width = int(input("What is the width of the rectangle :"))
# area = length * width
# print(f"the area of the rectangle is {area}")
# #create a program that swaps the value of two variables
# a = input("Enter the value of a :")
# b = input("Enter the value of b :")
# a,b = b,a
# print (f"After swapping a = {a}, b = {b}")
# #convert temp from celcius to fahrenheit.(celsius *9/5)+32)
# celsius = int(input("Enter temperature in Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius} C is equal to {fahrenheit} F")
# # #convert temp from fahrenheit to celcius
# fahrenheit = int(input("Enter temperature in Fahrenheit: "))
# celsius = (fahrenheit - 32) * 5/9
# print(f"{fahrenheit} F is equal to {celsius} C")

#CREATE A PYTHON LIST WITH AT LEAST 10 ELEMENTS
# my_list = [10,20,30,40,50,60,70,]
# #append an item to the list
# my_list.append(80)
# #remove an item from the list
# my_list.remove(30)
# #sort the list in ascending order
# my_list.sort()
# # length of the list
# length = len(my_list)
# print(length)
# #find the two items in the middle of the list
# number = my_list[2:4]
# print(number)
# #reverse the list using slicing method
# reverse = my_list[::-1]
# print(my_list)
# print(reverse)

# # CREATE A PYTHON DICTIONARY REPRESENTING A PERSON WITH KEYS LIKE 'name', 'age', and 'country'.
# my_dict = {"name" : "Ahmed", "age" : 18, "country" : "Saudia Arabia"}
# # access and print specific values from the dictionary
# name = my_dict.get("name")
# age = my_dict.get("age")
# country = my_dict.get("country")
# print(name)
# print(age)
# print(country)
# # # add a new key-value pair to the dictionary
# new_information = {"gender" : "male" }
# my_dict.update(new_information)
# print(my_dict)
# # # check if a specific key exists in the dictionary
# country = ("age",18) in my_dict.items()
# print(country)
# # # remove a key-value pair from the dictionary
# del my_dict["name"]
# print(my_dict)

# # CREATE A TUPLE CONTAINING THE NAMES OF YOUR FAVOURITE FRUITS.
# tuple_of_fruits = ("pinneaple", "watermelon", "grapes", "dragon fruit", "kiwi")
# # access individual elements of the tuple
# print(tuple_of_fruits[0])
# print(tuple_of_fruits[1])
# #  use slicing to extract a subset of fruits from the tuple
# fruit_subset = tuple_of_fruits[0:3]
# print(fruit_subset)
# # check if a specfic fruit exists in the tuple
# fruit_exists = "kiwi"in tuple_of_fruits
# print(f"does kiwi exists in the tuple of fruits : { fruit_exists}")


# # CREATE 2 SETS WITH SOME COMMON AND SOME UNIQUE ELEMENTS
# set1 = {1,2,3,4,5,6,7,}
# set2 = {6,7,8,9,10}
# # # find the intersection of the two sets
# intersection_set = set1.intersection(set2)
# print(intersection_set)
# # # find the union of the two sets
# union_set = set1.union(set2)
# print(union_set)
# # # add elements to a set
# set1.add(11)
# print(f"after adding 11 to set1 : {set1}")
# # # remove elements from a set
# set2.remove(9)# 
# print(f"after removing 9 from set2 : {set2} ")

# AGE VERIFICATION : 
# age = int(input("Enter your age :"))
# if age > 18:
#     print("You are eligible to vote.")
# else:
#     print("You are not eligible to vote.")

# USER AUTHENTICATION
# username = input("Enter your username :")
# password = input("Enter your password :")
# if username == "admin" and password == "admin123":
#     print("Grant admin privileges")
# else:
#     print("Deny admin privileges")

# NUMBER COMPARISON
# number1= int(input("Enter the first number :"))
# number2 = int(input("Enter the second number :"))
# if number1 > number2:
#     print(f"{number1} is greater than {number2}")
# elif number1 < number2:
#     print(f"{number1} is smaller than {number2}")  
# else:
#     print(f"{number1} and {number2} are equal")

# CHOOSING A MEAL AT A RESTAURANT
# preference = input("Enter your dietary preference (Vegetarian or Non-vegetarian): ")

# if preference == "Vegetarian":
#     print("You can choose from our vegetarian menu.")
# elif preference == "Non-vegetarian":
#     print("You can choose from our non-vegetarian menu.")
# else:
#     print("Invalid preference.")

# CHOOSING WHAT TO WEAR BASED ON THE WEATHER
# weather = input("Enter the current weather condition (Sunny, Rainy, or Snowy): ")
# if weather == "Sunny":
#     print("You should wear light and comfortable clothes.")
# elif weather == "Rainy":
#     print("Don't forget to bring an umbrella and wear a raincoat.")
# elif weather == "Snowy":
#     print("Bundle up in warm layers and wear a winter jacket.")
# else:
#     print("Please enter a valid weather condition.")

#1
# number = int(input("Enter the endpoint number :"))
# i = 1
# while i <= number:
#     if i %2 == 0:
#         print(i)
#     i+=1

# # 2
# number = int(input("Enter the endpoint number :"))
# i = 20
# while i >= number:
#     if i %2 == 0:
#         print(i)
#     i-=1

# 3
# numbers = [1,4,6,9,10]
# i = 0

# while i < len(numbers):
#     print(f"Square of {numbers[i]}: {numbers[i] ** 2}")
#     i += 1

# 4
# n = int(input("Enter a positive integer: "))
# sum_n = 0
# i = 1

# while i <= n:
#     sum_n = sum_n + i 
#     i += 1

# print(f"The sum of the first {n} natural numbers is {sum_n}")

# Create a program that calculates the sum of all even numbers from 1 to 50 using a for loop
# sum_of_even = 0
# for i in range(1,51):
#     if i  %2  == 0:
#         sum_of_even+= i
#         print(f"the sum of even numbers from 1 to 50 : {sum_of_even}")

# Ask a user to enter no. of rows and columns and create a mathematical table from the input 
# row = int(input("Enter the number of rows: "))
# col = int (input("Enter the number of columns: "))
# for i in range(1,row+1): 
#     for x in range(1,col+1):
#         print(f"{i * x :5} ",end='')
#     print()

#  Write a program that checks the user input(string format) and print the letters of the string
# user = input("Enter any word: ")
# for i in(user):
#     print(i)

# . Write a program that checks on odd numbers using (break and continue) and print out the results
# for i in range(1,15):
#     if i %2 == 0:
#         continue
#     print(i)
#     if i == 9:
#         break

# What is the result of the bitwise AND operation between 5 (binary 0101) and 3 (binary 0011)?
# A = 5
# B = 3
# print(A & B)

# What is the result of the bitwise OR operation between 6 (binary 0110) and 2 (binary 0010)?
# C = 6
# D = 2
# print(C | D)

#  What is the result of the bitwise XOR operation between 4 (binary 0100) and 1 (binary 0001)?
# E = 4
# F = 1
# print(E ^ F)

# If the binary representation of 7 is 00000111, what is the result of applying bitwise negation (~) to 7 assuming an 8-bit system? , elaborate the result of the output compared to the result of (~7).


# def left_shift_and_compare(x,n):
#     left_shift_value= x << n
#     multiplication_value = x * 2**n
#     return left_shift_value > multiplication_value
# x = 5
# n = 3
# result = left_shift_and_compare(x,n)
# print(result)

# def right_shift_even_odd(x,n):
#     right_shift_value = x >> n
#     if right_shift_value %2 == 0:
#         return "even"
#     else:
#         return "odd"
# x = 45
# n = 2
# result = right_shift_even_odd(x,n)
# print(result)

# def create_table(rows,columns):
#     for i in range(1,rows+1): 
#         for j in range(1,columns+1):
#             print(f"{i * j :5} ",end='')
#     print()
# def final():
#     rows = int(input("Enter the number of rows : "))
#     columns = int(input("Enter the number of columns : "))
#     create_table(rows,columns)
# final()


# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Division by zero is not allowed"

# def calculator():
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
#     operation = input("Choose an operation (+, -, *, /): ")
    
#     if operation == "+":
#         result = add(num1, num2)
#     elif operation == "-":
#         result = subtract(num1, num2)
#     elif operation == "*":
#         result = multiply(num1, num2)
#     elif operation == "/":
#         result = divide(num1, num2)
#     else:
#         result = "Invalid operation"
    
#     print(f"The result is: {result}")

# calculator()

import random


def guessing_game(secret_number):
    guess = None
    attempts = 0
    
    while guess != secret_number:
        guess = int(input("Guess the secret number: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low, Try again.")
        elif guess > secret_number:
            print("Too high, Try again.")
    
    return attempts  

def main():
    secret_number = random.randint(1, 100)  
    print("Welcome to the Guessing Game!")
    attempts = guessing_game(secret_number)
    
    print(f"Congratulations! You guessed the correct number in {attempts} attempts.")


main()

