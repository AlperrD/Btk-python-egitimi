kurum = 'Btk Akademi'.split() # Stringi boşluklara göre listeye çevirme.
#kurum = ['BTK', 'Akademi']

print(type(kurum))
print(kurum)
print(kurum[0])

sayilar = [1,2,3,4,5]
isimler = ['alper', 'mehmet', 'ali', 'zeynep', 'ayşe']

print(type(sayilar)) # sayilar değişkenin tipi nedir
print(type(sayilar[0])) # sayilar değişkenin içindeki 0. indeksteki elemanın tipi nedir.

print(type(isimler))
print(type(isimler[1]))


ogrenci = ['mehmet', 'kızılelma',59,37,100]

adSoyad = ogrenci[0] + ' ' + ogrenci[1]
ortalama =(ogrenci[2]+ ogrenci[3]+ ogrenci[4]) / 3
print(f'öğrenci adi: {adSoyad} | ögrenci not ortalaması: {round(ortalama,2)}') # round ile ondalık yuvarlama yaptık.

ogrenciler = [['mehmet', 'kızılelma',59,37,100], ['ali', 'demir',100,37,100]]

print(ogrenciler[0][1]) # öğrenciler listesinin ilk öğrencinin soyadı
print(ogrenciler[1][1]) # öğrenciler listesinin ikinci elemanındaki öğrencinin soyadı


# listelerle işlemler

programlama_dilleri = ['python', 'c++', 'c', 'java', 'javascript']

print(len(programlama_dilleri)) # eleman sayisi hesaplama

sonuc = programlama_dilleri[4] = 'flutter' # 4. elemanındaki değeri değiştirme.

print(programlama_dilleri) # liste olarak yazdırma

sonuc = programlama_dilleri + ['Deneme', 'Deneme']

kontrol = 'c++' in programlama_dilleri # liste içerisinde 'c++' var mı kontrolü
print(kontrol)

for i in sonuc: # liste içerisindeki her bir elemanı alt alta yazdırma.
    print(i)