import math
print("--- PART_1 ---")

x=0.335
y=0.025
z=32.005

a=int(input("Enter a: "))
b=x*(math.sin(math.atan(z)+math.cos(y))**2)
function_y=(a**2)*math.cos(b*x)-(b**3)*math.sin(a*x)*math.sqrt(math.exp(a*x+b))
print("Result of function: ",function_y)
print("")
print("--- PART_2 ---")
a1=0.5
b1=2.9
x1=0.3

F1=math.sqrt(a*x*math.sin(2*x)+(math.exp(-2*x))*(x+b))
F2=(math.cos((x**x)**2)-x)/math.sqrt((a**2)+(b**2))
print("Result of function F1: ",F1)
print("Result of function F2: ",F2)
F11=int(F1)
F22=round(F2)
print("The value of the variable F11: ", F11)
print("The value of the variable F22: ", F22)

new_x1=5
new_x2=11
new_y1=-1
new_y2=0
NALEZH1 = F11 >= new_x1 and F11 <= new_x2;
NALEZH2 = F22 >= new_y1 and F22 <= new_y2;
print("")
print("F1 є [", new_x1, ",", new_x2, "] is -> " , NALEZH1)
print("F2 є [", new_y1, ",", new_y2, "] is ->" , NALEZH2)




