# 1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.
markalar = ['Toyota', 'Bmw', 'Renault', 'Mercedes']

# 2- Liste kaç elemanlıdır.
print(len(markalar))

# 3- listenin ilk ve son elemanı nedir ?
print(f'Listenin ilk elemanı: {markalar[0]} | Listenin son elemanı: {markalar[-1]}')

# 4- 'Renault' markasını 'Togg' ile güncelleyiniz.
index = markalar.index('Renault')
markalar[index] = 'Togg'
print(markalar)

# 5- 'Togg' listenin bir elemanı mıdır.
sonuc = 'Togg' in markalar
print(sonuc)

# 6- Listenin ilk iki elemanını alınız.
print(markalar[:2])

# 7- Listenin sonuna ford ve citroen markalarını ekleyiniz
markalar = markalar +  ['Ford','Citroen']
print(markalar)

# 8- Listenin son elemanını siliniz.
del markalar[-1]
print(markalar)

# Öğrenciler listesi oluştur
ogrenciler = []
ogrenci1 = 'Yigit Bilgi 2010 [70,80,90]'
ogrenci2 = 'Ada Bilgi 2011 [70,70,80]'
ogrenci3 = 'Çınar Turan 2017 [60,60,90]'

def ogrenci_bilgi_parcala(ogrenci):
    # Veriyi boşluklardan ayır
    parts = ogrenci.split()
    
    # İsim, soyisim ve doğum yılı
    isim = parts[0]
    soyisim = parts[1]
    dogum_yili = int(parts[2])
    
    # Notlar kısmını listeye dönüştür
    notlar = parts[3].strip("[]").split(",")
    notlar = list(map(int, notlar))  # Notları int olarak listeye çevir
    
    # Sonucu döndür
    return [[isim, soyisim, dogum_yili, notlar]]

ogrenciler = ogrenci_bilgi_parcala(ogrenci1) + ogrenci_bilgi_parcala(ogrenci2) + ogrenci_bilgi_parcala(ogrenci3)
print(ogrenciler)

# ogrencilerin yaşlarını hesaplayınız. 

def yas_hesapla (ogrenci):
    ogrenciyas = 0
    ogrenciyas = 2024 - ogrenci[2]
    return ogrenciyas

def not_ortalam_hesapla (ogrenci):
    ortalama = 0
    for i in ogrenci[3]:
        ortalama += i
    return ortalama/3


ogrenci1yas = yas_hesapla(ogrenciler[0])
ogrenci2yas = yas_hesapla(ogrenciler[1])
ogrenci3yas = yas_hesapla(ogrenciler[2])

ogrenci1not = not_ortalam_hesapla(ogrenciler[0])
ogrenci2not = not_ortalam_hesapla(ogrenciler[1])
ogrenci3not = not_ortalam_hesapla(ogrenciler[2])

print(f"{ogrenciler[0][0]+ ' '+ ogrenciler[0][1]} | yaşı {ogrenci1yas} | not ortalaması: {ogrenci1not}")
print(f"{ogrenciler[1][0]+ ' '+ ogrenciler[1][1]} | yaşı {ogrenci2yas} | not ortalaması: {ogrenci2not}")
print(f"{ogrenciler[2][0]+ ' '+ ogrenciler[2][1]} | yaşı {ogrenci3yas} | not ortalaması: {ogrenci3not}")

# ogrencilerin not ortalamalarını hesaplayınız. 

# def not_ortalam_hesapla (ogrenci):
#     ortalama = 0
#     for i in ogrenci[3]:
#         ortalama += i
#     return ortalama/3


ogrenci1not = not_ortalam_hesapla(ogrenciler[0])
print(ogrenci1not)