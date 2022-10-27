class Bank:
    def rateofIntrest(self):
        return 0

class XBank(Bank):
    def rateofIntrest(self):
        return 10

class YBank(Bank):
    def rateofIntrest(self):
        return 12

obj=XBank()
print(obj.rateofIntrest())

obj1=YBank()
print(obj1.rateofIntrest())
