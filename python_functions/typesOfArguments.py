print("Demo abot Arguments");

def argudemo(i,j):
    print(i,j)

argudemo(5,3)        # positional arguments print as per intialize order
argudemo(j=5,i=45)   # keyword Arguments  we can explicitly called with arguments

# Example 2:

def argdemo2(i,j=10):
    print(i,j)

argdemo2(40)     # default value access from default position arguments
argdemo2(5,4)    # if we declare with in call the latest value overcome existing value


# Example 3:    Keyword Argument demo to print
def greeting(name,greetmsg):
    print(greetmsg+" "+name)

greeting(greetmsg="Hi!",name="Darling")

# Example 4:     combination of positonal and keyword
def my_fun(a,b,c):
    print(a,b,c)

my_fun(10,20,30)
my_fun(a=10,b=20,c=40)
my_fun(10, c=30, b=40)
#my_fun(c=40, b=20, 10)



    # revision of 4 data types
def tupledemo():
    print("Tupel Demo")
    mytuple = (10, 'Anil', 'city', 23 )
    print(type(mytuple))
    print(mytuple)
    print(mytuple[2])
    for i in mytuple:
        print(i)

tupledemo()

def listDemo():
    print("Let's List Demo")
    mylist = ["anil", "varma", 25]
    print(type(mylist))
    print(mylist)
    for i in mylist:
        print(i)
listDemo()

def setDemo():
    print("Demo Set")
    myset = {"anil", 'varma', 25}
    print(type(myset))
    print(myset)
    for i in myset:
        print(i)
setDemo()

def dictDemo():
    print("Dictionaries Demo")
    mydict = {
    "name" : "Anil",
    "age"  :    24,
    "village": "kodakandla"
    }
    print(type(mydict))
    print(mydict)
    for x,y in mydict.items():
        print(x,y)

dictDemo()

