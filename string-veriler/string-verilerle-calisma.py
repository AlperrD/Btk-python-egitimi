kursAdi = 'Python ile Programlama'
kursAciklama = 'Güzel bir kurs'
kursSuresi = '20 saat'

mesaj = 'Kurs Adi: ' + kursAdi + '\n' + 'Kurs Açıklaması: ' + kursAciklama + '\n' + 'Kurs Süresi: ' + kursSuresi

print(mesaj)

# String Slicing 

print(kursAdi[0])       # ilk indeksteki değeri verir.
print(kursAdi[-1])      # sonuncu indexteki değeri verir.

print(kursAdi[0:6])     # Baştan 6. indekse kadar alır. 6 dahil değildir.
print(kursAdi[:6])      # baştan 6. indekse kadar alır. 6 dahil değildir.
print(kursAdi[6:])      # 6.indexten sonuna kadar alır.


print(kursAdi[7:10])    # 7.index ile 9. indeksi dahil eder. 10. indeksi almaz.

print(kursAdi[0:6:1])   # bir karakter atlayarak alır. Hepsini alır.
print(kursAdi[:6:2])    # iki karakter atlayarak alır. 1 alır bir almaz.
print(kursAdi[:-1])     # baştan başlayıp son karaktere kadar alır son karakter dahil değildir.
print(kursAdi[:: -1])   # Tersten yazdırır.
print(kursAdi[-11:])    # -11 den başlayarak -1'i de dahil ederek alır.


adet = len(kursAdi)
print(adet)


# String Concat (Formatlama)

ad = 'Alper' 
soyad = 'Duman'
yas = 23

msj = "My name is " + ad + " "+ soyad  + " " + "I'm " + str(yas) + " years old. " 
print (msj)

# format kullanarak yapılası. 

mesajj = "My name is {1} {0} I'm {2} years old.".format(ad, soyad , yas) # eğer süslü parantez içinde index belirtmezsek format sırasıyla alır. Bir tanesine belirtirsek diğerlerine de belirtmemiz gerekmektedir.

print(mesajj)

a = f"My name is {ad} {soyad} I'm {yas} years old." # En pratik yolu f String'dir.
print(a)


# String uygulaması 

title = "Python ile Programlama Dersleri"

# title değişkeni karakter sayisi 
print(f'Karakter Sayisi: {len(title)}')
# title değişkeni içerisinden 'Python' kelimesini alın
print(title[:6])
# title değişkeni içerisinden ilk 5 ve son 5 karakteri alın
print(f'title değişkenindeki ilk 5 karakter: {title[:6]} | son 5 karakter: {title[len(title)-5:]}')
# title değişkenini tersten yazdırınız.
print(f'title değişkeninin tersten yazılmış hali {title[::-1]}')

# klavyeden değerler alarak öğrenci bilgisini yazdırınız.

orgAd = input('Öğrenci adını ve soyadını bir boşluk bırakarak giriniz.')
ogrNot1 = float(input('Öğrencinin almış olduğu ilk notu giriniz.'))
ogrNot2 = float(input('Öğrencinin almış olduğu ikinci notu giriniz.'))
notOrt = (ogrNot1 + ogrNot2) / 2

print(f'{orgAd} adlı öğrencinin 1. notu: {ogrNot1} | ikinci notu: {ogrNot2} | not ortalaması: {notOrt} ')