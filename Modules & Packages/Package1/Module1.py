def fun1():
    print("This is fun2 from Module 2")
    mytupele=('ANil',"varma",25)
    print(type(mytupele))
    print(mytupele)
    for i in mytupele:
        print(i)

def fun2():
    print("List Example .....")
    mylist=['Anil',"varma",25]
    print(type(mylist))
    print(mylist)
    for i in mylist:
        print(i)
    print(mylist[2])

def fun3():
    print("Set Examples.........")
    myset={"Anil",'varma',25}
    print(type(myset))
    for i in myset:
        print(i)
def fun4():
    print("Dictionary class/data type Example.....")
    mydict={
        "name":"Anil",
        "job":"Tester",
        "age":25
    }
    print(type(mydict))
    print(mydict)
    for i in mydict:
     print(i)

fun1()
fun2()
fun3()
fun4()
