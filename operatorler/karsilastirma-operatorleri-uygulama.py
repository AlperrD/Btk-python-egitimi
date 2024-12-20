# girilen iki sayıdan hangisi daha büyüktür.

sayi1 = int(input("birinci sayıyı giriniz: "))
sayi2 = int(input("ikinci sayiyi giriniz: "))
sonuc = 0

def buyukSayiHesapla (sayi1, sayi2) :
    if sayi1 > sayi2:
        print(f'{sayi1} büyüktür.')
    else: print(f'{sayi2} büyüktür.')

buyukSayiHesapla(sayi1, sayi2)

# girilen bir sayının tek çift kontrolü yapınız.

def tekCiftKontrol (sayi1, sayi2):
    if sayi1 % 2 == 0:
        print(f'{sayi1} çift sayıdır.')
    else: print(f'{sayi1} tek sayıdır.')

    if sayi2 % 2 == 0:
        print(f'{sayi2} çift sayıdır.')
    else: print(f'{sayi2} tek sayıdır.')


tekCiftKontrol(sayi1, sayi2)


# bir öğrencinin girilen 3 notuna göre başarı durumunu kontrol ediniz. 50 ve üstü başarılı.

not1 = int(input("1.not"))
not2 = int(input("2.not"))
not3 = int(input("3.not"))

notOrt = (not1+not2+not3) / 3

if notOrt >= 50: 
    print(f'{notOrt} ile dersten geçtiniz.')
else: print(f'{notOrt} ile dersten kaldınız.')


