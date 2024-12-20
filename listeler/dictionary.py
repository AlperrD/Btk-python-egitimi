# key - value tipinde veriler saklanır. 41 : "Kocaeli"
# Sıralanabilir, güncellenebilir, veriler tekrarlanmaz (Key).

# sehirler = ['kocaeli' , 'istanbul']
# plakalar = [41,34]

# print(plakalar[0], sehirler[0])
# print(plakalar[1], sehirler[1])

# print(plakalar[sehirler.index('istanbul')])
# print(plakalar[sehirler.index('kocaeli')])


plakalar = {
    'kocaeli': 41, 
    'istanbul': 34,
    'izmir':36
    }

plakalar['izmir'] = 35

print(plakalar['kocaeli']) 
print(plakalar['istanbul'])
print(plakalar['izmir'])



ogrenciler = {
    101: {
        "Ad": "Yiğit",
        "Soyad": "Bilgi",
        "DogumYili" : 2010,
        "Notlar" : (40,80,90)
    },
    202: {
        "Ad": "Ada",
        "Soyad": "Bilgi",
        "DogumYili" : 2012,
        "Notlar" : (80,80,90)
    },
    303: {
        "Ad": "Yiğit",
        "Soyad": "Bilgi",
        "DogumYili" : 2017,
        "Notlar" : (70,70,70)
    }

}

ogrenciNo = int(input('Öğrenci no: '))

ogrenci = ogrenciler[ogrenciNo]

ogrenciNot = (ogrenci['Notlar'][0]+ogrenci['Notlar'][1]+ogrenci['Notlar'][2] )/3

print(f"{ogrenciNo}'lu,{ogrenci['Ad']} {ogrenci['Soyad']} ismindeki öğrencinin. Doğum yılı: {ogrenci['DogumYili']}'dir. Not Ortalaması ise: {round(ogrenciNot,2)}'dur... ")
# round fonksiyonu virgülden sonra kaç basamak istediğimizi belirlemek için kullanılır.


# konsoldan girilen değerlerle öğrenci sözlük yapısına yeni veriler ekleme.

ogrenciIndex = int(input('Ogrenci index giriniz: '))
ogrenciAd = input('Ogrenci adını ve soyadını aralarında bir boşluk bırakarak giriniz: ')
ogrenciDogumYili = int(input('Ogrenci doğum yılını giriniz: '))
ogrenciNot = input('Ogrenci notlarını aralarında bir boşluk bırakarak giriniz.')
ogrenciAd = ogrenciAd.split()
ogrenciNot = ogrenciNot.split()
ogrenciler[ogrenciIndex] = {"Ad":ogrenciAd[0],"Soyad":ogrenciAd[1],"DogumYili":ogrenciDogumYili,"Notlar":(int(ogrenciNot[0]),int(ogrenciNot[1]),int(ogrenciNot[2]))}

print(ogrenciler[ogrenciIndex])
print(ogrenciler[101])



