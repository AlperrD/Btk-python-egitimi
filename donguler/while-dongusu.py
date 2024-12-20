# for => list 
# while => koşullu

# sayilar = [1,2,3,4,5,6,7,8,9]
# i=0
# while (i<len(sayilar)):
#     print(sayilar[i])
#     i += 1

# for i in sayilar:
#     print(i)

# 1 Başlangıç ve bitiş değerlerini kullanıcıdan alarak bu değerler arasındaki tüm çift sayıları yazdırın.

# baslangic = int(input("Baslangıc değeri: "))
# bitis = int(input("Bitis değeri: "))

# while (baslangic <= bitis):
#     if(baslangic%2 == 0):
#         print(baslangic)
#     baslangic += 1

baslangic = 10
bitis = 9
while (baslangic <= bitis):
    if(baslangic%2 == 0):
        print(baslangic)
    baslangic += 1

ad = "alper"

print(ad.upper())