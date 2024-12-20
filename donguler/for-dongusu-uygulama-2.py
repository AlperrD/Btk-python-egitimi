urunler = [
    {"urunAdi": "Hp Victus 1", "fiyat": 32999},
    {"urunAdi": "Lenovo ThinkPad", "fiyat": 25999},
    {"urunAdi": "Apple Macbook", "fiyat": 49999},
    {"urunAdi": "Huawei Matebook", "fiyat": 26999},
    {"urunAdi": "Casper Nirvana", "fiyat": 20000},
    {"urunAdi": "Hp Victus 2", "fiyat": 30000},
]

# Hp Victus marka ürünün fiyatı .. tl dir. hepsine uygula.

for i in urunler:
    print(f"{i["urunAdi"]} marka ürünün fiyatı: {i["fiyat"]} Türk Lirası'dır.")


# ürünlerin fiyatlarının toplamı nedir.

toplam = 0

for i in urunler:
    toplam += i["fiyat"]
print(f"Ürünlerin toplam fiyatı {toplam}₺ ")

# 25000 tl ile 40000 arasındaki ürünleri listele.

print("filtre uygulandı.")
for i in urunler:
    if(i["fiyat"] >= 25000 and i["fiyat"] <= 40000):
        print(f"{i['urunAdi']} : {i['fiyat']}")


# Kullanıcıdan alınan anahtar kelimeye göre ürünleri listele.

aramaDegeri = input("Filtrelemek için ürün girin.").lower()
for i in urunler: 
    if aramaDegeri in i["urunAdi"].lower():
        print(f"aradığınız değere göre bulunan ürünler {i['urunAdi']} : {i['fiyat']}")

    
# in yerine find kullanırsak sadece 3 kelimelik metinde ilk kelimede aranılan değer var ise 0 döndürür fakat in kullanırsak aranılan değer listenin herhangi bir yerinde var ise sonuç döndürülür.