class Myclass:
    __a=25
    def display(self):
        print(self.__a)

class Yourclass:
    def display2(self):
        print("this is display method")


o1=Myclass()
o1.display()
o2=Yourclass()
o2.display2()


#print(Myclass.__a)  # we cant access bcoz it private variable

class Miclass:
    def __disp2(self):    # private method
        print("This is private method")

    def disp3(self):
        print("This is public method")
        self.__disp2()

ob=Miclass()
ob.disp3()
# ob.__disp2()  # it is giving error :: 'Miclass' object has no attribute '__disp2'


# Example 3: read values from private class out side of the class

class Myclasses:
    __empid=101
    def getempid(self,eid):
        self.__empid=eid

    def dispalyempid(self):
        print(self.__empid)

obj5=Myclasses()
obj5.getempid(105)
obj5.dispalyempid()