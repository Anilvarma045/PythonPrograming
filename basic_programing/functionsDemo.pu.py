print("Lets create Function");


def simple_function():
    print("Hello This is Anil")


def simple_function2(name):
    print("my name is" + name)


def simple_Multiarguments(*names):
    print("my common names are"+names)

def simple_unknownnumberof_Arguments(**names):
    print("My LastName is "+names["lname"])


#def simple_arrayListMethod()
def my_function(food):
  for x in food:
   print(x)

fruits = ["apple", "banana", "cherry"]



simple_function()
simple_function2("ANilVarma")
simple_unknownnumberof_Arguments(fname="Anil", lname="varma")
my_function(fruits)

#simple_Multiarguments("Anil","varma","Krishna") 
