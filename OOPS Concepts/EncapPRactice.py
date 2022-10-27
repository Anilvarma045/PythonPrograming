class Fclas:
        __empid=101                      # this is private variable
        def  getempid(self,eid):
            self.empid=eid
            pass
        def displayemp(self):               # this variable intialized here with another method vaiable

            print(self.eid)

obj=Fclas()
obj.displayemp()