#Berilgan to'rt xonali son raqamlarining ko'paytmasi   topilsin.
x=int(input("4 xonali son kiriting:"))
print((x%10)*((x%100)//10)*((x%1000)//100)*(x//1000))