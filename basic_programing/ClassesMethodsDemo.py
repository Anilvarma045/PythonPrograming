
class Student:

    nameinni="Resume"
    def __init__(self,m1,m2,m3):
        self.m1=m1;
        self.m2=m2;
        self.m3=m3;
    def avg(self):
        return (self.m1+self.m2+self.m3)/3;
  # @classmethod
    def info(cls):
        return cls.nameinni;

    def represent(self):
        c=self.m2-self.m3;
a1=Student(20,30,40);
a2=Student(30,40,60);
print(a1.avg());
print(a2.avg());
print(a1.info());