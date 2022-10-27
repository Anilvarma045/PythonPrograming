print("Variable Demo")

# Example 1:
global_vari=20


def fun():
    local_var="Anil"
    print(global_vari)
    print(local_var)

fun()
# print(local_var)   # local variable are not accessible out side of function
print(global_vari)   # global variable Access everywhere
# Example 2
xy=100
def fun2():
    xy=200   #local varible
    print(xy)        # when we have local global have same name the value will print local variable only

fun2()


def fun3():
    global xy
    xy=200  #global variable  by using global keyword above Statement
    # global xy=200    # this is invalid in Python
    print(xy)

fun3()
print(xy)    # this is modified by above funtion by using global keyworde

x=120

# Example 4:
def fun4():
    global x
    x=150
    print(x)

fun4()
print(x)

def fun5():
    global y   # we can define a global variable with in a class with the help of global
    y=277
    print(y)

fun5()
print(y)    # it define with in a function as a global keyword  it can accessed as global tooo.