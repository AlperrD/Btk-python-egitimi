isim = 'Alper'
yas = 7
kilo = 15.5
ogrenciMi = True

print(type(isim))    # Str
print(type(yas))     # int
print(type(kilo))    # Float
print(type(ogrenciMi)) # bool 

print("Adı: " + str(isim) + " Yaş: " + str(yas) + " Kilo: "+  str(kilo)+ " ögrenci Mi: " + str(ogrenciMi))


# Veri tipi dönüşümleri 

a = int("10")   # int fonksiyonuna 10.5 gibi değer gönderirsek string olarak hata verir.
a = int(10.5)   # bu kısım çalışır.
a = float(10) 
a= float("10")  # ama float fonksiyonuna gönderdiğimiz değer string olarak da int olarak da tamsayı olarak gönderirsek sıkıntı olmaz. 
print(a)

# yani sadece int fonksiyonu float veri tipinde String olarak gönderilen (int ('10')) gibi verilerde tip hatası verir.


'''
    Uygulama 1: Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız.
    alan: pi*r^2
    çevre: 2.pi.r

    uygulama 2: Klavyeden girilen km bilgisini mil cinsinden hesaplayınız.
    mil = km/ 1.609344

'''

pi = 3.14159
yaricap = float(input('Dairenin yarı çapını veriniz: '))

alan = yaricap*yaricap*pi
cevre = float(yaricap) * pi * 2

print('Girdiğiniz yarıçapa göre alan: ' , alan,  'Girdiğiniz yarıçapa göre çevre: ', cevre )


km = float(input('km giriniz'))

mil = km/ 1.609344
mil = round(mil, 2) # Ondalık yuvarlama.

print('girdiğiniz km için hesaplanan mil değeri: ' ,mil )

