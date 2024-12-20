liste = ["1" ,"3" , "5" , "30b" , "abc" ,"0","99", "981f"]
# liste elemanları içindeki sayısal değerleri bulunuz


# for i in liste:
#     try:
#         sonuc = int(i)
#         print(sonuc)
#     except ValueError:
#         continue


# 2 kullanıcı "q" değerine bastığında ve sayı değeri girdiğinde döngüyü sonlandır aksi halde devam et.

# while True:
#     sayi = input("Sayi:")
#     if sayi == "q":
#         break

#     try:
#         sonuc = float(sayi)
#         print(f"Girilen sayi {sonuc}")
#         break
#     except ValueError:
#         print("Geçersiz sayi")
#         continue


# dict ve key bilgilerini parametre olarak alan get (dict, key) fonksiyonunu hazırlayınız. (KeyError)

urun = {"urunAdi": "iphone 15", "urunFiyat" : 25000}

def getir (liste, key):
    try:
        return liste[key]
    except KeyError:
        return None
    
print(getir(urun, "urunAdi"))
print(getir(urun, "fiyat"))