# we should import module for existing one
# Approach 1
import calcularor
calcularor.add(100,200)
calcularor.mul(10,30)

# Approach 2

from calcularor import add,mul
add(20,30)
mul(3,10)

# Approach 3

from calcularor import *
add(5,4)
mul(6,5)