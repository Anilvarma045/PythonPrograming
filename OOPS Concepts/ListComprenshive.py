
square = [i**2 for i in range(1,6)]
print(square)
for x in square:
    print(x)

list1 = [1,3,5,7]
list2 = [2,4,6,8]
[(1,2),(3,4),(5,6),(7,8)]
pair = [(x,y) for x in list1 for y in list2 if x!=y]

for x,y in pair:

    print(pair)