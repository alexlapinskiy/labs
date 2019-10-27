import math

x=0.335
y=0.025
z=32.005

a=int(input("Enter a: "))
b=x*(math.sin(math.atan(z)+math.cos(y))**2)
function_y=(a**2)*math.cos(b*x)-(b**3)*math.sin(a*x)*math.sqrt(math.exp(a*x+b))
print("Result of function: ",function_y)