# Return ifadesi. 
def toplam():
    return 10 + 20

sonuc = toplam()
print(sonuc)

def yil():
    import datetime
    return datetime.datetime.now().year

def yasHesapla():
    return yil() - 2001

yas = yasHesapla()
print(yas)


def saat():
    import datetime
    return datetime.datetime.now().hour

# Selamlama fonksiyonu
def selamla():
    if(saat() <= 12):
        print("Gunaydın")
    else: print("Merhaba")

selamla()


