import math
x=int(input(("xni kiriting: ")))
print(math.sin(x)+math.sqrt(abs(x-5)) if x<5 else (5.45**2*math.cos(math.pi)+math.log(x+2)) if x==5 else ((x-5)**2*math.tan(x/2)))