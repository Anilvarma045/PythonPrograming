# 1 way to create Function  simple function take parameters
def sum(start,end):
    result=0;
    for i in range(start,end+1):
        result=result+i;
    print(result)
    return(result)
sum(10,20)

def mul(start,end):
    if(start>end):
        print("Start should be less then end")
