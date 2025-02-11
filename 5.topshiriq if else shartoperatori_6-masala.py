n=int(input("nechta son kiritmoqchisiz:"))
a=[0]*n
for i in range(n):
    a[i]=int(input(f"{i+1}-elementni kiriting: "))
print(a)
count=0
for i in range(n):
    if(a[i]<0):
        count+=1
print(f"massivda {count} ta manfiy son mavjud")

# manfiy = list(filter(lambda x: x < 0, [(lambda x: int(input(f"{x+1}-elementni kiriting: ")))(i) for i in range(int(input("nechta son kiritmoqchisiz:")))]))
# print(manfiy)