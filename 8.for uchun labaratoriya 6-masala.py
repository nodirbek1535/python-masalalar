n=int(input("nechta son kiritmoqchisiz: "))
a=[]  
for i in range(n):
    a.append(int(input(f"{i+1}-elementni kiritng: ")))
b=[]
for j in a:
    if j<0:
        b.append(j)
if b:
    print("eng katta manfiy son: ", max(b))
else:
    print("manfiy sonlar mavjud emas")

