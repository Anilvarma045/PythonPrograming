print("Dictionary Demo");

mydict = {"Name:" : "Anil", "Age":25,   "Gender:":"Male"}
print(mydict)
print(type(mydict))

# Accessing values from Dictionary
mydict1 = {
        'brand':'Hyundai',
        'Model':'i20',
        'year':2022
}
print(mydict1)
# if we want particular set of dict we need use key as parameter
print(mydict1['Model'])

# by using get() function to get value
print(mydict1.get('brand'))

# change values in dictionary
mydict1['year']=2020
print(mydict1)
for i in mydict1:   # it Retrun only Keys
    print(i)

# read key and values by Using looping stmt
for i in mydict1:
    print(mydict1[i])    # this will print only Values from Dictionary

for i in mydict1.values():
    print(i)

for x,y in mydict1.items():
    print(x, y);

mydic = {
    'code' : 56,
    'item c': 'hardware',
    'price' : 2000
}
# check key is existing or not by using If Condition
if 'code' in mydic:
    print("exist")
else:
    print("not Exist")

print('price' in mydic)    # it will return true/false

# add items into the Dictionary
mydic['colour'] = "Red"
print(mydic)

# Remove item from Dictionary
# mydict.pop("year")      # delete only year key and value
# del mydict              # it will delete Entire dict
# del mydict["year"]
# mydict.clear()          # it will clear entire items in list


# copy one dict to another dict by copy() method
mydict2=mydict1.copy()
print(mydict2)

# without using copy() method it will be Same
