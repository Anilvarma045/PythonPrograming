

print("Im introducing tuples here")

# different ways to write tuple and access values from tuples

mytuple1 = ('Anil', 'varma', 'kumar', 'her', 'villain', 'rowdy', 'sideActor')
print(type(mytuple1))  # it is displays type of data type
print(mytuple1[1])  # it is access particular index value
print(mytuple1)  # it is displayed all values in tuple
print(mytuple1[-1])  # it is displayed negative mean index start from back
print(mytuple1[2:5])  # it will display only index given that range
print(mytuple1[3:])  # it's print start from  after 3 index
print(mytuple1[:3])  # it will print only before value of index 3
tuple2 = ('ANil', 'farray', 'Ramesh')
if "ANil" in tuple2:
    print("yes, Anil in this tuple list")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# create another tuple and copy values from one list to another list
mytuple3 = ("hhh", "okay", "bbb")
ylist = list(mytuple3)
ylist[2] = "apple"
mytuple3 = tuple(ylist)
print(ylist)
print(mytuple3)
print(len(mytuple3))
# tuple is unchangeable so if we want change anything we should convert to list
# print(mytuple3[2].remove)
y = list(mytuple3)
y.remove("hhh")
print(y)
