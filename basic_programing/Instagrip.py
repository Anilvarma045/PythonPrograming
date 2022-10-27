class User:
    def __init__(self,a,b):
        self.a=a;
        self.b=b;

    def myStatus(self):
        c=self+self.b;
        print(c);
        print(self.a);
User(5,7).myStatus(20);

class Student:
    def __init__(self,m1,m2):
        self.m1=m1;
        self.m2=m2;
    def avg(self):
        return (self.m1+self.m2)/2;
a1=Student(20,30);
a2=Student(30,40);
print(a1.avg());
print(a2.avg());
