import copy

li1=["Anil","varma"]
print(li1)
print("norrmally by using Assignment Operator");
li2=li1
print(li2)
li2.append("Kumar")
print(li1)
print("li2 is:", li2)

print(" then we are going use Deep copye")
#A deep create a new copund of object before inserting copies of the items found in the orginal into it in recursive manner
#Note: in deep copy any changes made copy of the object do not reflect in the orginal object,

li3=[1,2,"Anil"]
print("list before copy",li3)
li4=copy.deepcopy(li3)
print("deep copy object: ",li4)
li4.append("hero")
li3.append("5")
print("li 3 is after append on li4",li3)
print("li 4 is after append on li4",li4)

print(" lets discourse about shallow copy");
li5=[1,2,[3,4],5]
li6=copy.copy(li5)
print("li 5",li5, "li6: ",li6)
print("the original elements before shallow copying")
for i in range(0,len(li5)):
    print(li5[i],end=" ")
print("\r")

# adding Elements in newly create list mean li6
li6[2][0]=7
print("check the change any happend in original list")
for i in range(0,len(li5)):
    print(li5[i],end=" ")
print("\ acctually we are making changes in li6 bocz of copy() it happend in orginal too")
