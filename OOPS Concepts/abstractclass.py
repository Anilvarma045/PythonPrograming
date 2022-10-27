from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Tiger(Animal):
    def eat(self):
        print("this is eat raw meat")

class  Cow(Animal):
    def eat(self):
        print("Eat Veg")

obj1=Tiger()
obj2=Cow()

obj1.eat()
obj2.eat()