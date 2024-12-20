# yaşı 18 den büyük ya da veli izni varsa bir işte çalışabilir durumunu kontrol ediniz.
yas = 1
izin = False
sonuc = yas > 18 or izin == True

print(f'İşte Çalışma durumunuz: {sonuc}')


# ders notu 50 - 100 arasındaysa geçti aksi halde kaldı yazdırsın.

dersNot = 1

sonuc = (dersNot > 0 and dersNot< 101) and (dersNot >= 50 )
print(f'Dersten geçme durumunuz: {sonuc}')

# not ortalaması en az 70 ve zayıfı yoksa teşekkür alabilme durumunu kontrol edin.

nott = 70
zayif = True

sonuc = nott >= 70 and zayif == False
print(f'Teşekkür belgesi alabilme durumunuz. {sonuc}')

# işe girmek için önlisans veya lisans mezunu olacak ve sigara kullanmayacak 
mezun = 'lisans'
sigara = False
sonuc = (mezun == 'lisans' or mezun =='onlisans') and  sigara != True
print(f'İşe girme durumu: {sonuc}')

# uygulamaya giriş kontrolü username ya da mail ve parola

username = 'username'
mail = 'maill'
parola = '123'

sonuc = (username == 'username' or mail == 'mail') and parola == '1293'

print(f'giriş yapabilirsin {sonuc}')

