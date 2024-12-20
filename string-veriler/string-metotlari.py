mesaj = 'BTK Akadami , python Kursu'

sonuc = mesaj.upper() # Hepsini büyük harf yapar.
print(sonuc)
sonuc = mesaj.lower() # Hepsini küçük harf yapar.
print(sonuc)
sonuc = mesaj.title() # Her kelimenin sadece ilk harfini büyük yapar.
print(sonuc)
sonuc = mesaj.capitalize() # Cümlenin ilk harfini büyük yapar diğerlerini küçültür. 
print(sonuc)

# CTRL + k + c = Yorum satırı yapma | CTRL + k + u = Yorum satırı kaldırma

sonuc = 'abc'.islower() # True
print(sonuc)
sonuc = 'AbC'.isupper() # False
print(sonuc)

print(mesaj)
sonuc = mesaj.strip() # Baştaki ve sondaki boşlukları kaldırır.
print(sonuc)

sonuc = mesaj.split() # Kelime aralarındaki boşluklara göre cümleyi kelime kelime böler. .split()[0] 0. indexteki kelimeyi getirir. 'BTK'
print(sonuc)

sonuc = mesaj.split(',') # Gireceğimiz özel harf vs. ile ayırma yapar.
print(sonuc)

sonuc = mesaj. startswith('B') # Girdiğimiz harfin başlangıç harfi olup olmadığını söyler (Büyük küçük harf duyarlıdır.) "B ile mi başlıyor."
print(sonuc)

sonuc = mesaj.index('Kursu')    # aradığımız kelimenin hangi indexten başladığını söyler. // ör/ kursu ifadesi 21.indexten başlar.
print(sonuc) 

sonuc = mesaj.endswith('u')     # ör/ mesaj değişkenimizin içindeki metin "u" ile mi bitiyor.
print(sonuc)

sonuc = mesaj.replace('python', 'java')     # ilk ifadede bulduğu değeri bizim yazdığımız ikinci değer ile değiştirir. (karakterlerin veya belirli bir harfin değiştirilmesini yapabiliriz. 'a','e' gibi.)
print(sonuc)


# String Metodları çalışma örnekleri

kursAdi =  "Btk Akademi Python ile Programlama Dersleri"
website = "https://www.btkakademi.gov.tr/"

# 1- ' Btk akademi ' dizesindeki başındaki ve sonundaki boşlukları siliniz.
metin = ' btk akademi '
print(metin.strip()) # baştaki ve sondaki boşlukları kaldırma.

# 2- kursAdi değişkenindeki tüm karakterleri küçük harfe çevirin.
print(kursAdi.lower())

# 3- website değişkeninde kaç tane '.' karakteri vardır.
print(website.count('.'))

# 4- website değişkeni 'https' ile mi başlıyor.
print(website.startswith('https'))

# 5- website 'tr' ile mi bitiyor
print(website.endswith('tr'))

# 6- kursAdi içerisindeki tüm karakterler harflerden mi oluşuyor.
print(kursAdi.isalpha()) # boşluk olduğu için false verir isalphanum ise sayılar ve harflerden oluşuyor ise true verir.
a = 'adsdndjksd3 ' # sayı ve harf varsa true boşluk vs varsa false
print(f'alfanümerik kontrol: {a.isalnum()}')

# 7- kursAdi içerisindeki tüm boşlukları '_' ile değiştirin
degistir = kursAdi.replace(' ', '_')
print(degistir)

# 8- kursAdi içerisindeki python kesimesini ReactJs ile değiştir.
print(kursAdi.replace('Python', 'ReactJs'))# birden fazla replace kullanabiliriz.

# 9- website değişkeni 'www' içeriyor mu
print(website.__contains__('www')) 
# find ve index ile de bulunduğu indexi kontrol edebiliriz ikisinin arasındaki fark find arayıp bulamaz ise -1 döndürür index ise hata geri döndürür.

# 10- kursAdi değişkeni listeye çevirin
degisim = kursAdi.split()
print(degisim)


