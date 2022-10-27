from abc import ABC,abstractmethod

class Cal(ABC):
    def __init__(self,value):
        self.value=value    #now  it is class variable

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def sub(self):
        pass

class Con(Cal):
    def add(self):
        print(self.value+100)

    def sub(self):
        print(self.value-10)

obj=Con(100)    # this value for constructor constrctor take valu from class and intialied when object created for classa
obj.add()  #200
obj.sub()  #90
