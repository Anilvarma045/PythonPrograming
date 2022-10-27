class A:
    def m1(self):
        print("Im from A my name M1")

class B(A):
    def m1(self):
        print("Im from B my name is M1")
        super().m1()
obj=B()
obj.m1()


# Example New:

class Ab:
    a,b=20,30

class Ba(Ab):
    i,j=56,80
    def m12(self,x,y):
        print(x+y)
        print(self.i + self.j )
        print(self.a * self.b)
obj1=Ba()
obj1.m12(100,200)

# Examp 3
# over riding the variable value

class parent:
    name='Anil'
    #print("myname")
class child(parent):
    name='Varma'
    print("myname")
obj2=child()
print(obj2.name)
m22=parent()
print(m22)