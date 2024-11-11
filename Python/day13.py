import math
import random

def calc1(x,y):
    math1 = math.pi * x **y
    return math1

def calc2(q):
    math2 = math.sqrt(q)
    return math2


def guessing_game():
    trial = 3
    starting = 1
    guess_no = random.randint(1,3)
    while starting <= trial:
        guess =  input("Guess the number :")
        if  guess == guess_no:
            print("You won!!")  
        else:
            print(f"try again")
            starting +=1
    
guessing_game()
 