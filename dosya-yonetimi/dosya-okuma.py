# dosya açmak ve oluşturmak için open() metodu kullanılır. Dosya erişme modu tanımlayabiliriz. Dosyayı okuma veya yazma vs hangi amaçla açtığımızı belirttiğimiz kısımdır.

# Dosya oluştur ve veri yaz
# with open("deneme.txt", "w") as f:
#     f.write("Bu, log dosyasındaki örnek metindir.")

f = open("deneme.txt","r")
# print(f.read())
# f.seek(5) # cursor indexini veririz ve o satırdan altını okur. Sırasıyla her bir karakter indexini ilerletir. alper deneme alt alta ise seek değerini 6 verirsek çıktımız eneme olur.
# print(f.read())
# f.seek(0)

# print(f.readlines()) # dizi olarak verir.
# f.seek(0)
print(f.readline()) # verilen indexe kadar olan harfleri verir. Ondan sonrakileri vermez.

f.close()