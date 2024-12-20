# kendisine gönderilen bir kelimeyi belirtilen kez ekranda yazdıran bir fonksiyon yazınız.

# def kereYaz(kelime, tekrar):
#     for i in range (tekrar):
#         print(kelime)
# kereYaz("Alper", 10)

# Dikdortgenin alanı ve çevresini hesaplayan fonksiyonu yazınız.

# def alanVeCevreHesapla (kısaKenar, uzunKenar):     
#     return f"Dikdörtgenin alanı = {a*b} : Dikdörtgenin Çevresi = {2*(a+b)}"
    
# a = int(input("Alan hesaplamak için uzun kenar: "))
# b = int(input("Alan hesaplamak için kısa kenar."))

# print(alanVeCevreHesapla(b,a))


# Yazı tura uygulamasını fonksiyon kullanarak yapınız Random() kullanarak. 

# def yazıTura (tahmin):
#     import random
#     sonuc = random.randint(0,1)

#     if sonuc == tahmin:
#         print("Doğru tahmin.")
#     else:
#         print("yanlış tahmin")

# yazıTura(0)

# Kendisine gönderilen iki sayı arasındaki tüm asal sayıları bulan fonksiyonu yazın.

# def asalSayiBul (sayi1,sayi2): 
#     for sayi in range(sayi1, sayi2 +1):
#         if sayi > 1:
#             for i in range(2, sayi): # Mevcut sayıya kadar bölen yoksa else ile sayıyı yazdır (Asal Durum) eğer varsa break ile döngülerden çık sonraki sayıya geç.
#                 if(sayi % i == 0):
#                     break
#             else:
#                 print(sayi)
                

# asalSayiBul(0, 100)

# Kendisine gönderilen bir sayının tam bölenlerini bulan fonk yaz.

# def tamBolenBul (sayi):
#     tamBolenler = []
#     for i in range (2,sayi):
#         if (sayi % i == 0):
#             tamBolenler.append(i)

#     return tamBolenler
# print(tamBolenBul(10))

