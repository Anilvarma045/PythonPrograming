print("THis is Starting point of program")
print("THis is Starting point of program")
print("THis is Starting point of program")


try:
    print(x)
except:
    print("chance to exception arise")
else:
    x=10
    print(x)

print("this is end of the program...")
print("this is end of the program...")
print("this is end of the program...")
print("this is end of the program...")


# Example Two(2)

print("this is starting of the prgoram")
print("Under progress")
try:
    print(10/1)
except ZeroDivisionError:
    print("THis is exception throw ZERO DIVISION ERROR")
print("program is completed")


# EXAMPLE: 3   multiple thrown exception 1 try block support many expect block
try:
    num,num2=10,1
    result=num/num2

    print("result is :",result)
except ZeroDivisionError:
    print("Thrown Exceptin")
except SyntaxError:
    print("thrown Syntax error exception....")

else:
    print("No exception occured....")
finally:
    print("i tried exception handling Statements")


# Example : Raise our Own Exception:
def enterage(num):
    if num<0:
        raise ValueError("only integers are allowed")

    else:
            print("enter only Integer value")
    if num%2==0:
        print("even")
    else:
        print("Odd Number")

print("checking number is even or odd by calling any ")


print("                   ")
enterage(20)
enterage(0)     # it accept only integer values  # it is under raised Exception if give is not integer its through exception.
num=1
try:
    enterage(num)
except ValueError:
    print("value error exception occured and handled....")


