

# demo of polymorphism
class Human:
    def sayhello(self,name=None):
        if name is not None:
            print("Hello" + name)
        else:
            print("hello")

obj=Human()
obj.sayhello("ANil")
obj.sayhello()

# Exampele OVerRide 2

class calculation:
    def add(self, a=0,b=0,c=0):
        print(a+b+c)

cal=calculation()
cal.add()
cal.add(12,20,30)
cal.add(100,200)