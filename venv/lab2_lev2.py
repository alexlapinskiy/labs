import math

print("--- RECTANGLE ---")
a=int(input("Enter width: "))
b=int(input("Enter length: "))
s=a*b
p=2*(a+b)
print("Area of rectangle = ",s)
print("Primetr of rectangle = ",p)

print ("")
print("--- TRIANGLE ---")
a1=float(input("Enter 1 side of triangle: "))
b1=float(input("Enter 2 side of triangle: "))
c1=float(input("Enter 3 side of triangle: "))
p1=float((a1+b1+c1)/2)
h_a1=float((2/a1)*math.sqrt(p1*(p1-a1)*(p1-b1)*(p1-c1)))
h_b1=float((2/b1)*math.sqrt(p1*(p1-a1)*(p1-b1)*(p1-c1)))
h_c1=float((2/c1)*math.sqrt(p1*(p1-a1)*(p1-b1)*(p1-c1)))

print("h_a of triangle = ",h_a1)
print("h_b of triangle = ",h_b1)
print("h_c of triangle = ",h_c1)

print ("")
print ("--- FUNCTION_1 ---")
x=1.45
y=-1.22
z=3.5
f_b=1+(z**2/3+(z**2)/5)
function_a=(2*math.cos(x-(math.pi/6))*b)/((1/2)+math.sin(y)**2)
print("Result of function: ", function_a)

print ("")
print ("--- FUNCTION_2 ---")
x=1.2
y=-0.8

f_z=(math.sin(x)**3)+(math.cos(y)**2)
function_s=1+x+((x**2)/math.factorial(2))+((x**3)/math.factorial(3))+((x**4)/math.factorial(4))
print ("Result of funtion: ",function_s)