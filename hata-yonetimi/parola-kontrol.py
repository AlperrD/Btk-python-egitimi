
# Eğer parola içinde türkçe karakter varsa hata fırlat

def parolaKontrol (parola):
    turkceKarakterler = "çğışİüÜÖö"
    
    for i in parola:
        if i in turkceKarakterler:
            raise TypeError("Parolada Türkçe karakterler kullanılamaz.")
        

    print(f"Geçerli parola: {parola}")


while True:
    parola = input("Kontrol için parola giriniz.")

    try:
        parolaKontrol(parola)
    except TypeError as e:
        print(e)
        continue