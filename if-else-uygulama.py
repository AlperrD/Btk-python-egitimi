yakit_ucretleri = {"benzin": 49.35, "dizel": 41.71, "lpg": 20.28}
mesafe = int(input("Kat ettiğiniz mesafe nedir: "))
arac_yakit_tipi = input("Yakıt tipinizi belirtin: (benzin,dizel ya da lpg)")
toplam_yakit_tuketimi = (float(input("100 km de ortalama yakıt tüketimi nedir.")) / 100) * mesafe

if(arac_yakit_tipi == "benzin"):
    toplam_ucret = yakit_ucretleri["benzin"] * toplam_yakit_tuketimi
    print(f"Toplam masraf: {toplam_ucret}")
elif(arac_yakit_tipi == "dizel"):
    toplam_ucret = yakit_ucretleri["dizel"] * toplam_yakit_tuketimi
    print(f"Toplam masraf: {toplam_ucret}")
elif(arac_yakit_tipi == "lpg"):
    toplam_ucret = yakit_ucretleri["lpg"] * toplam_yakit_tuketimi
    print(f"Toplam masraf: {toplam_ucret}")
else:
    print("yanlış değerler verildi.")