# age = int(input("Enter your age :"))
# gender = input("Enter your gender : ")
# religion = input("Enter your religion : ")
# # conditional execution
# if age > 18:
#     if gender == "female" and religion == "muslim":
#         print("you are welcome")
#     else:
#         print("You are not allowed to attend this party!!")
# else:
#     print("you are under age!")

# check age,country and gender
# age = int(input("Enter your age :"))
# country = input("Enter your country :")
# gender = input("Enter your gender : ")
# # conditional execution
# if age > 20:
#     print("You are allowed")
# elif country == "kenyan" and gender == "male":
#     print("You are welcome")
# else:
#     print("You are not allowed")

# nested
age = int(input("Enter your age :"))
if age > 18:
    country = input("Enter your country :")
    gender = input("Enter your gender : ")
    if  country == "kenya" and gender == "male":
        print("You are allowed")
    else:
        print("not allowed") 
else:
    print("You are not allowed")
    
