import math

print("--- RECTANGLE ---")
a=int(input("Enter width: "))
b=int(input("Enter length: "))
s=a*b
p=2*(a+b)
print("Area of rectangle = ",s)
print("Primetr of rectangle = ",p)

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
