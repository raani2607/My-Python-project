# decoraters -> a function that extends the behaviour of another function without actually modifying the base function


def yesterday(kenty):
    def spices(*args, **kwargs ): #used for not specifying
        print("you ordered pizza")
        kenty(*args, **kwargs)
    return spices



def today(kenty):
    def flavour(*args, **kwargs ): #used for not specifying
        print("with margaritta")
        kenty(*args, **kwargs)
    return flavour








@yesterday
def eating_food(choice):  #base function
    print(f"thanks for the meal, the {choice} was tasty")

eating_food("pizza")