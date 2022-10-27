# i gone be practicing Encapsulation

class  ANil:
    def anil(self):
        self.a=10
        print("THis is encpasualted class")

class   Kumar(ANil):
    def kumar1(self):
        print("this is my last name")
        print(self.a)
c=Kumar()
c.anil()
c.kumar1()