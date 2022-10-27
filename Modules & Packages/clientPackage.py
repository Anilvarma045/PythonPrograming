import sys
sys.path.append("C:/Users\DELL\PycharmProjects\pythonPrograming\Modules & Packages\Package1")

import Module1
import Module2

Module1.fun1()
Module2.fun2()


# Approach 2
# it show only error but its run correct>  JUST pYCHAR UNABLE TO FIND IT
from Module1 import *
from Module2 import  *

fun1()
fun2()
