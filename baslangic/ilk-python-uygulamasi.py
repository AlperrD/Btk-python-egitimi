print('Yeni bir başlangıç')

# Değişken tanımlama. 

urunAFiyat = 4000
urunBFiyat = 5000

kdvOrani = 0.20

print('A ürünü Kdvli fiyat: ' , (urunAFiyat*kdvOrani)+urunAFiyat)
print('B ürünü Kdvli fiyat: ', (urunBFiyat*kdvOrani)+urunBFiyat)

urunToplami = urunAFiyat + urunBFiyat
print('toplam fiyat: ' , urunToplami )

urunToplamiKdvli = urunToplami + urunToplami * kdvOrani
print('toplam Kdvli fiyat: ' ,  urunToplamiKdvli )

# Değişken tanımlama kuralları.
# 3sayi = 60 => değişken isimleri sayi ile başlayamaz.

# sayi3@ = 60 => değişkenler içerisinde sadece '_' kullanilir.

# urunFiyati = 1000 camelCase
# urun_fiyati = 1000 

# komut isimlerinden 'True vs' kullanmamalıyız.


x =y = z = 20


# degiskenler örnek uygulama. 

ad, telefon, eMail, il = 'Alper Duman', '02541522541','info@gmail.com','Kocaeli'

mouseAd, mouseFiyat = 'Kablosuz Mouse', 550
klavyeAd, klavyeFiyat = 'Kablosuz Klavye',650
bilgisayarAd, bilgisayarFiyat = 'Dizüstü Bilgisayar',55000

toplamUcret = mouseFiyat + klavyeFiyat + bilgisayarFiyat

toplamKdv = toplamUcret * 0.18

print(ad,'Toplam ödediği Miktar ',toplamUcret)
print('Toplam KDV: ' , toplamKdv)
