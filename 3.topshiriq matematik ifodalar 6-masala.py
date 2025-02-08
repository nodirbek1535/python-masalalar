import math
x=float(input("x ni kiriting:"))
y=float(input("y ni kiriting:"))
z=float(input("z ni kiriting:"))
b=math.sqrt(10*(math.pow(x,1/3)+math.pow(x,y+2)))*(math.asin(z)**2-abs(x-y))
print(b)
