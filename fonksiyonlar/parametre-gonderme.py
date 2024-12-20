def yasHesapla(dogumyili):
    return 2024 - dogumyili

def emeklilikHesapla (dogumYili, isim):
    yas = yasHesapla(dogumYili)

    kalanYil = 65 - yas

    if kalanYil > 0:
        return f"Sayın {isim}, emekliliğinize {kalanYil} yıl kalmıştır."
    else: return f"Sayın {isim}, zaten {abs(kalanYil)} önce emekli oldunuz." # abs mutlak değer fonksiyonudur.


print(emeklilikHesapla(2001,"Alper"))