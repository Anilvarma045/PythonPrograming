# Abstract Demo Practice

from abc import ABC,abstractmethod

class Mynames(ABC):
    @abstractmethod
    def display(self):
       pass

    @abstractmethod
    def printname(self):
        None
  #   @abstractmethod    we can call without annotation but if abstarct method must bedefine with in a Sub class
    def printnick(self):
        print("Varma")

class Varma(Mynames):
    def display(self):
        print("this is abstract class method")

    def printname(self):
        print("MY name is anil")


x=Varma()
x.display()
x.printname()