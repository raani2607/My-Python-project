class father ():
    def add(self):
        print("this is the addition block")
        x = int(input("enter your first number: ")) 
        y = int(input("enter your second number: "))
        calc = x + y
        print(calc)
class mother(father):
# obj = father()
# obj.add()
    def sub(self):
        print("this is the subtraction block")
        z= int(input("enter your first number: ")) 
        k = int(input("enter your second number: "))
        calc1 = z - k
        print(calc1)

class child(mother):
      def div(self):
        print("this is the division block")
        a= int(input("enter your first number: ")) 
        b = int(input("enter your second number: "))
        calc2 = a - b
        print(calc2)

obj =  child()
obj.sub()
obj.div()
obj.add()

