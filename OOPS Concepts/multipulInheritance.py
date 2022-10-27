# multipul inheritance have two pairent for 1 child class

class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B:
    a,b=20,30
    def m2(self):
        print(self.a * self.b)

class C(A,B):
    i,j=40,30
    def m3(self):
        print(self.i - self.j)

obj=C()
obj.m1()
obj.m2()
obj.m3()