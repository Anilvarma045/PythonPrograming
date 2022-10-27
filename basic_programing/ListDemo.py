
print("List Demo")
mylist = [10, 20, 30, 40, 50, 0.45]

mylist2= ["ANil", "Varma", "Kumar"]

mylist3 = ["anil", 25, 'M']

# Print values from list
print(mylist)
print(mylist2)
print(mylist3)

# EXAMPLE 2: Access values from List
fruits = ["banana", "Apple", "orange", "cylinder", "rococo", "jamb ist"]

print(fruits[1])
print(fruits[-1])

# Range of Index
print(fruits[1:3])
print(fruits[-2:-5])
fruits[3] = "Robot Fruits"    # it replace Existing Value
print(fruits)

# use for loop to print in sequence
for i in fruits:
    print(i)

# use condition to check item is within list or not
if "banana" in fruits:
    print("Yes banana in the Mylist")
else:
    print("no banana is not in List")

# find Length of list by len function
print(len(fruits))

# add items using append() and insert() methods
my_names = ["anil", "Kumar", "varma"]
my_names.append("aanil")    # adding new item in list

my_names.insert(2,"cherry") # by using insert method we customize location
print(my_names)

# Remove item from list using pop function and del keyword
my_names.pop(4)    # delete with pop keyword
print(my_names)

del fruits[2]   # delete with del keyword
print(my_names)

# clear method clears the Entire items in list print variable only
# my_names.clear();
print(my_names)

# copy list one list to another list
fruits2 = list(fruits)      # method 1 with direct initialize method
print(fruits2)

# using copy() function
fruits3 = fruits2.copy()
print(fruits3)

# ex:10 joins the Multiple List
# suing = operator
list1 = [1, 2, 2]
list2 = ['A', 'B', 'C']
list3 = list1 + list2
print(list3)

# using loop to join List
for i in list1:
    list1.append(i)
print(list1)

# using extend() fuction join Lists
list1.extends(list3)
print(list1)

