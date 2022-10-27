import sys
sys.path.append("C:/Users\DELL\PycharmProjects\pythonPrograming\Modules & Packages\PackageA")
sys.path.append("C:/Users\DELL\PycharmProjects\pythonPrograming\Modules & Packages\PackageB")

import Emp       # Emp is a module from Package A
empobj=Emp.Employee(101,'ANil',45000)
empobj.empDetails()

import stu          # import stu module from package B by using path
from stu import *

stuobj=Student(105,'Ponnam',8)
stuobj.studetails()
