import math
import cmath
print("--- PART_1 ---")
my_list=[1,2,3,4,5,6,7,8,9,10]
a=int(input("Enter the limit a: "))
b=int(input("Enter the limit b: "))
i=0
product1=1
product2=1
length = len(my_list)
for i in range(length):
    if (i<a-1):
        product1*=my_list[i]
    elif (i>=b and i<length):
        product2*=my_list[i]
print("Product = ",product1*product2)

print("")
print("--- PART_2 ---")
x=float(input("Enter value x:"))
y=float(input("Enter value y:"))
z=float(input("Enter value z:"))
h=float(input("Enter value of step:"))
a=0
b=[1,2,3,4,5,6,7]
f=7
print("--- Cycle FOR ---")
print("Value X ", "\t", " Value Y ", "\t", " y = f(x)")
for a in b:
    if  x>0 and y>0:
        function=(cmath.asin(z)**2)+(x+y)
        x+=h
        y+=h
        print("\t", x, "\t", "\t", y, "\t", "\t", function)
    else:
        print("Check entered values, they must be more than 0")
print("----------------------------------------------------------")

new_x=x
new_y=y
function=0
a=0
print("--- Cycle WHILE ---")
while a<f:
    if  new_x>0 and new_y>0:
        function=(cmath.asin(z)**2)+(x+y)
        a+=h
        new_x+=h
        new_y+=h
        print("\t", new_x, "\t", "\t", new_y, "\t", "\t", function)
    else:
        print("Check entered values, they must be more than 0")