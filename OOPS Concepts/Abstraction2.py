from abc import ABC, abstractmethod

class X(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
    @abstractmethod
    def m3(self):
        pass

class Y(X):
    def m1(self):
        print("this is m1")
    def m2(self):
        print("THis is m2 method")

class Z(Y):
    def m2(self):
        print("THis is m2 from Z")
    def m3(self):
        print("this is m3 for verification")
# y=Y()     :TypeError: Can't instantiate abstract class Y with abstract method m2
z=Z()
z.m2()
z.m1()
z.m3()
