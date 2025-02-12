#0 dan 15 gacha bo’lgan sonlarni ikkilik ko’rinishini chop qiluvchi programma tuzilsin.
a=int(input("son kiriting: "))
s=""
while a>0:
    s+=str(a%2)
    a//=2
print(s[::-1])