# 1. Misol: Setdagi elementlarni tartibga solish
# Berilgan setni o'sish tartibida saralash va uning minimal va maksimal qiymatini topish.
# Vazifa:
# •	Setni o'sish tartibida tartibga soling.
# •	Setdagi eng kichik va eng katta elementni toping.

sonlar={1,2,2,1,3,2,1,4,5,3,2,4,5,3,2,5,6,6,44,3,2,3,5,6,7654,43,987,45,43}
print("toplam:",sonlar)


# •	Setni o'sish tartibida tartibga soling.
tartiblash_list_tipida=sorted(sonlar)
print("tartiblangan toplam:",tartiblash_list_tipida)


# •	Setdagi eng kichik va eng katta elementni toping.
print("maksimum element:",max(tartiblash_list_tipida))
print("minimum element:",min(tartiblash_list_tipida))


# 2. Misol: Setda takrorlanmaydigan elementlarni aniqlash
# Berilgan ro'yxatda takrorlanmaydigan elementlarni aniqlang.
# Vazifa:
# •	Ro'yxatni setga aylantirib, takrorlanmaydigan elementlarni aniqlang.
sonlarsanoq={}
for son in sonlar:
    if son in sonlarsanoq:
        sonlarsanoq[son]+=1
    else:
        sonlarsanoq[son]=1

faqat_bir_marta_kelgan_sonlar=[]
for son in sonlar:
    if sonlarsanoq[son]==1:
        faqat_bir_marta_kelgan_sonlar.append(son)
print("faqat_bir_marta_kelgan_sonlar:",faqat_bir_marta_kelgan_sonlar)


# 3. Misol: Setdagi elementlarni o'zaro farqlash
# Berilgan ikkita setdan birining elementlari ikkinchisida mavjud bo'lmaganlarini topish.
# Vazifa:
# •	Birinchi setdagi elementlar, ikkinchi setda mavjud bo'lmaganlarini toping.
# •	Ikkinchi setdagi elementlar, birinchi setda mavjud bo'lmaganlarini toping.
sonlar1={1,2,2,1,3,2,1,4,5,3,2,4,5,3,2,5,6,6,44,3,2,3,5,6,7654,43,987,45,43,-1,-453,-12345,-5,-87}
sonlar={1,2,2,1,3,2,1,4,5,3,2,4,5,3,2,5,6,6,44,3,2,3,5,6,7654,43,987,45,43,9,9,9,0,0,0,11111}

# •	Birinchi setdagi elementlar, ikkinchi setda mavjud bo'lmaganlarini toping.
birtoplamdamavjudlar=sonlar-sonlar1
print("sonlar toplamida mavjud lekin sonlar1 toplamida mavjud bolmagan sonlar",birtoplamdamavjudlar)

# •	Ikkinchi setdagi elementlar, birinchi setda mavjud bo'lmaganlarini toping.
birtoplamdamavjudlar1=sonlar1-sonlar
print("sonlar1 toplamida mavjud lekin sonlar toplamida mavjud bolmagan sonlar",birtoplamdamavjudlar1)


# 4. Misol: Setlarni birlashtirib, unikal qiymatlarni topish
# Berilgan ikkita ro'yxatni setga aylantiring, ularni birlashtirib, faqat unikal qiymatlarni aniqlang.
# Vazifa:
# •	Ikkita ro'yxatni setga aylantirib, ularni birlashtiring.
# Birlashgan setdagi unikal qiymatlarni toping.
list1=[1,56,2,3,4,4,5,54,0]
list2=[2,35,65,434,224,1,0,6,4]
yigilganset=set()
#1-listni setga yigish
for i in list1:
    yigilganset.add(i)
#2-listni setga yigish
for i in list2:
    yigilganset.add(i)
print("setga aylantirilgan listlarning natijasi",yigilganset)

# 5. Misol: Setdagi elementlarni chiqarish (Pop)
# Setda bir nechta elementni pop (o'chirish) qilish, bunda o'chirilgan elementlarni chiqarish.
# Vazifa:
# •	Setdagi uchta tasodifiy elementni pop qilib, o'chirilgan elementlarni chiqarib yuboring.
import random
toplam={1,32,34,65,34,22,87,97,0}
for i in range(3):
    randomelement=random.choice(list(toplam))
    toplam.pop(randomelement)
print(toplam)


