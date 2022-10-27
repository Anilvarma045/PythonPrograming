class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

# here B is inherit properties from Class A
class B(A):
    a,b=20,30
    def m2(self):
        print(self.a * self.b)

# here  C is inherit properties from class A
class C(A):
    i,j=40,30
    def m3(self):
        print(self.i - self.j)

#object for B class B(A)
obj1=B()
obj1.m1()
obj1.m2()

# object for C class C(A)
obj2=C()
obj2.m1()
obj2.m3()
