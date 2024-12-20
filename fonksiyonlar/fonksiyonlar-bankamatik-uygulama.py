# 10.9 ve 10.10 kısımlarını tekrardan izle.

# Hesap bilgilerini tut. 
# menu, paraCekme, bakiyeSorgulama, paraYatirma fonksiyonları tamamlanacak.
# Çekilmeke istenen tutat hesapta yoksa ek hesabın kullanılmak istemediği sorulacak.

hesaplar = [
    {
        "ad" : "Alper Duman",
        "hesapNo" : "12345",
        "bakiye" : 20000,
        "ekHesap" : 5000,
        "ekHesapLimit": 5000,
        "username" : "AlpDuman",
        "password" : "1234",

    },
    {
        "ad" : "Ali Duman",
        "hesapNo" : "12345",
        "bakiye" : 20000,
        "ekHesap" : 10000,
        "ekHesapLimit": 10000,
        "username" : "AliDuman",
        "password" : "1234",

    },
]

def menu(hesap):
    print("\n")
    print(f"Merhaba {hesap["ad"]}")

    print("1- Bakiye Sorgulama")
    print("2- Para Çekme")
    print("3- Para Yatırma")

    islem = input("Yapmak istediğiniz işlem: ")

    if islem == "1":
        bakiyeSorgulama(hesap)
    elif islem == "2":
        paraCekme(hesap)
    elif islem == "3":
        paraYatirma(hesap)
    else:
        print("Yanlış Seçim.")

    menu(hesap)


def bakiyeSorgulama(hesap):
    print(f"Bakiye {hesap["bakiye"]} ₺")
    print(f"Ek bakiye {hesap["ekHesap"]}")

def paraCekme(hesap):
    miktar = float(input("Ne kadar para çekmek istersiniz: "))

    if hesap["bakiye"] >= miktar:
        print ("Paranızı çektiniz. Güle güle harcayın")
        hesap["bakiye"] -= miktar
    else: 
        toplam = hesap["bakiye"] + hesap["ekHesap"]
        if toplam >= miktar:
            ekHesapKullanimIzni = input("Paranızı çekmek için ek hesabınız kullanılsın mı? (e/h)")
            if ekHesapKullanimIzni == "e":
                kalanTutar = miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekHesap"] -= kalanTutar
                print ("Ek hesabınız kullanılarak para çekme işleminiz gerçekleştirildi.")
            if ekHesapKullanimIzni == "h":
                print("Hesap kullanım izni reddedildi. Para çekme işlemi başarısız.")
        else:
            print("Çekmek istediğiniz miktar hesaplarınızda bulunmuyor. Lütfen farklı bir tutarla tekrardan deneyiniz.")
 
def paraYatirma(hesap):
    miktar = float(input("Ne kadar yatırmak istersiniz. "))

    if hesap["ekHesap"] == hesap["ekHesapLimit"]:
        hesap["bakiye"] += miktar
        print(f"Hesabınıza {miktar} ₺ yatırıldı.")
    else:
        eksikTutar = hesap["ekHesapLimit"] - hesap["ekHesap"]
        hesap["ekHesap"] += eksikTutar
        print(f"ek hesabınıza {eksikTutar}₺ yüklendi.")
        miktar -= eksikTutar 
        if miktar > 0:
            hesap["bakiye"] += miktar
            print(f"ana hesabınıza {miktar}₺ yüklendi.")
    

def login():
    username = input("Username: ")
    password = input("password: ")

    isLoggedIn = False

    for hesap in hesaplar:
        if (hesap["username"] == username and hesap["password"] == password):
            isLoggedIn = True
            menu(hesap)
            break
    if not(isLoggedIn):
        print("username veya parola yanlış.")

login()