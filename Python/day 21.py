from abc import ABC,abstractmethod
class father(ABC):
    @abstractmethod
    def talking(self): #declaration
        pass  #nodefinition

        # print("Hay")  #declarartion
    @abstractmethod
    def chattinmg(self): #declaration
        pass


class mother(father):
    def talking(self): #declaration
        print("hello")

    def chatting(self): #declaration
        print("hello world")


class child(mother):
    def talking (self):  #declaration
        print("I am studying")

    def chatting(self): #declaration
        print("I am cchatting")
 

# father = father()
mother = mother()
child = child()

# father.talking()
mother.chatting()
mother.talking()
child.talking()
child.chatting()