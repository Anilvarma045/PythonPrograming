

# Example : 1

# Class Variable Demo

class Demo:
    name = "anil"
    age = 25
    a,b=2,3;  # this variables are called class variables

    def add(self):
        print(self.a +self.b)
        print(self.a * self.b)
# if we want Use class variable we should use self keyword with in a method.
call=Demo()
call.add()


# Example : 4 With create all types of variables
i,j=5,6             #global variable

class Myclass:
    a,b=7,8
    def add(self,x,y):
        print(x+y)       # x, y are local variable
        print(self.a + self.b)   # class variable we can access with self keyword
        print(i+j)       # global variables direct we can access
call1=Myclass()
call1.add(100,200)     # calling with local variables means parameters

# Example : 3

c,d=15,25  #global variable
class Demo3:
    c,d=12,22
    def add(self,c,d):
        print(c+d)   #local variable utilisation
        print(self.c+self.d)  # access class variables
        print(globals()['c']+globals()['d'])   # global variable access

call3=Demo3()
call3.add(30,40)

# Ex: 6   We can create multiple objects for one Class
class Demo4:
    def display(self,name):
        print(name+" this is my display method")
call4=Demo4()
call4.display("Hi!")
call5=Demo4()
call5.display("oye!")

#  method  & constructor Example

class democonstructor:
    def __init__(self):
        print("Hi! man This is Constructor")
    def meth1(self):
        print("Hello This is method Yaar")

    def meth2(self,x,y):
        print("meth2 is return type only")
        return(x + y)
call2=democonstructor()   # constructor will invoke automatically when object created
call2.meth1()
call2.meth2(11,22)