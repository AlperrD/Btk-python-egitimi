# Dictionary Metotları:

yemekTarifi = {

    "yemekAdi": "musakka",
    "YemekTarifi": "TarifAcıklaması",
    "resim":"  1.ppg"
}

# Girilen değerlere göre değer geri döndürür.
# Access item
sonuc = yemekTarifi["yemekAdi"] 
sonuc = yemekTarifi.get("yemekAdi")
sonuc = yemekTarifi.keys()
sonuc = yemekTarifi.values()
sonuc = yemekTarifi.items() # bir liste olarak geri döndürür. dict_items([('yemekAdi', 'musakka'), ('YemekTarifi', 'TarifAcıklaması'), ('resim', '  1.ppg')])

# Update Items:
yemekTarifi["yemekAdi"] = "manti" # öğe varsa itemi günceller yoksa ekler.
sonuc = yemekTarifi

yemekTarifi.update({"yemekAdi" : "MAnti"}) # Key olduğu için güncelleme yaptı. # bu da yoksa ekleme yapar.

yemekTarifi.update({"m":"m"})
sonuc = yemekTarifi

# Delete Items:
yemekTarifi.pop("yemekAdi") # İçine girilen değeri listeden siler.
sonuc = yemekTarifi

yemekTarifi.popitem() # parametre göndermeden listeye son eklenen itemleri siler.

yemekTarifi.clear()
sonuc = yemekTarifi


print(sonuc)