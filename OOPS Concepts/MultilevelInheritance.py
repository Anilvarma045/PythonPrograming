print("multi level inheritance")

class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=20,30
    def m2(self):
        print(self.a * self.b)

class C(B):
    i,j=40,30
    def m3(self):
        print(self.i - self.j)

obj3=C()
obj3.m1()
obj3.m2()
obj3.m3()