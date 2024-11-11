# overriding is  a way of letting method of a subclass overide the method of a superclass
# class Father():
#     def talking(self):
#         print("I am good in ....")

# class Child(Father):
#     def talking(self):
#         print("I am good in Italian")
#     # pass


# obj = Child()
# obj.talking()

# obj1 = Father()
# obj1.talking()

class Father():
    def talking(self):
        print("I am good in ......")

class Child(Father):
    def talking(self):
        print("I am good in Italian")

obj = Child()
obj.talking()  

obj1 = Father()
obj1.talking()  
