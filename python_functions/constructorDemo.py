
# constructor with Arguments
class Myclass:
    name="Anil"
    def __init__(self,name):     #Constructor with Arguments
        print(name+" HI program call constructor Argument")
        print(self.name +" this is calling from class variable")
mc=Myclass("Varma")

# Example 2:
class Emp:
   # eid=""
   # ename=""
    # esal=""

    def __init__(self, eid, ename, esal):
       # print(+eid, +ename, +esal)
        self.eid=eid          #this variable is now converted into class variable
        self.ename=ename
        self.esal=esal

    def display(self):
        print(self.eid, self.ename, self.esal)
call=Emp(121,"Anil",45000)
call.display()

# Example 3:   print data with constructor
class Student:
    def __init__(self,sid, sname):
        self.sid=sid
        self.sname=sname
    def __str__(self):
       # return(self.sid,self.sname)   # it is giving Error bcoz diffrent type data not printable in constructor
       # Above mehtod perfect for this constructor read with method
        return (self.sname)   # this string constructor call only String type.
stu=Student(12,'Anil')
print(stu)

