


class A:
    def m1(self):
        print("THis is m1 method from A")

class B(A):
    def m2(self):
        print("this is m2 method from Class B")

bobj=B()
bobj.m1()
bobj.m2()


# Example 2:
# inheritance with arguments

class My:
    x,y=10,20
    def m1(self):
        print(self.x,self.y)

class You(My):
    a,b=100,120
    def m2(self,age):
        print(self.a-self.b)
        print(age)
obj=You()
obj.m1()
obj.m2("Anil")


