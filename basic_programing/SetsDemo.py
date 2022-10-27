print("sets Demo")

# Example 1: Set Demo
myset = {"Apple", "Orange", "lemon"}
myset1 = ("Anil", 'hero', 'villan')
print(type(myset1))
for i in myset:
    print(i);

# Ex:2 value existed in set or not
print("banana" in myset)     # its Return True/False
print("Orange" in myset)        # it should return true

# Example: 3 Add items to set by adding() and update() method
# add()  update()
print(myset)
myset.add("grape")
print(myset)
# by using update() method we can Multiple values at Same Time
myset.update(["guvva", "Cherry"])
print(type(myset))
print(myset)
print(len(myset))
myset2 ={"anil", "varma", "kumar"}
myset2.remove("kumar")
# when we are using remove method not in set value its throw Key Error.
print(myset2)
myset.discard("prabhas")        # it is not throw any Error

# remove method remove all value from the Set it return empty SET
# myset.clear()
#del myset        # it will delete entire Set
# print(myset)      # it's Through Exception

# joins Two Set
# update() and union() method
myset3 = myset.union(myset1)
print(myset3)

myset2.update(myset3)
print(myset2)