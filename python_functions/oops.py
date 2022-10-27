class Myclass:
    def myfun(self):
        pass    # pass means nothing
    def display(self,greet):
        print(greet+ " Anil")

Myclass().display("Hi")    #calling a class object creation direct
mc1=Myclass()   # we can store with in variable too.
mc1.display("Hello")   #it will print code on display method

# Example: 2
class Myclass2:
    def m1(self):
        print("THis is instance method")
    @staticmethod
    def m2(self,name):
            print(name+" THis is static Method")
            print(self)
# invoke of static method
mc3=Myclass2()
mc3.m1()

mc3.m2("ANil","varma")    #here self consider as first Argument
Myclass2.m2("Anil","varma")
Myclass2.m2(25,26)

# Myclass2.m1()      # this call giving error why because its instance method

