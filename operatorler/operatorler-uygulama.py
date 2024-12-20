a,b,c = 4,8,(12,2)

# kullanıcıdan aldığınız iki sayının çarpımı ile a,b,c toplamının farkı nedir.

# sayi1 = int(input("Birinci sayıyı girin: "))
# sayi2 = int(input("İkinci sayıyı girin: "))

# sonuc = sayi1*sayi1 - (a+b+c[0]+c[1]) 

# c'nin b'ye kalansız bölümünü hesaplayınız.

sonuc = (c[0]+c[1])//b

# (a,b,c) toplamının mod 7'si nedir? 

toplam = a + b + c[0] + c[1]
print(toplam)

sonuc = toplam % 7

# b'nin a'ıncı kuvvetini hesaplayınız.

sonuc = b ** a

# a, *b, c = (2,4,6,8,13) işlemine göre c'nin küpü nedir.

a, *b , c = (2,4,6,8,13)  # (*b) demek tuple içindeki ilk değer a ya son değer c ye ve geri kalan değerler ise b' ye demektir.

sonuc = c**3

# a, b , *c = (2,4,6,8,13) bu işleme göre c değerlerinin toplamı nedir.

a, b , *c = (2,4,6,8,13)

sonuc = c[0] + c[1] + c[2]







print(sonuc)

