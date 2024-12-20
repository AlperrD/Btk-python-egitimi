sayilar = [1,2,3,4,10,20,40,50,90,5,5,5,5]
isimler = ['Ali', 'Alper', 'memet']

print(max(isimler))
print(min(isimler))
print(max(sayilar))
print(min(sayilar))

# ekleme

sayilar.append(100)
print(sayilar)
isimler.append('canan')
print(isimler)

sayilar.insert(0,20)
print(sayilar)

sayilar.insert(-1,200) # eklerken bulunan indexteki elemanları bir sağa kaydırır yani ikiyüz -2 elemana gelir.
print(sayilar)

sayilar.insert(-2,300)
print(sayilar)

sayilar.insert(len(sayilar),500) # şimdi son elemana ekleme yapar.
print(sayilar)

# silme 

sayilar.pop()  # default son değeri siler.
print(sayilar)


sayilar.pop(1)  # default son değeri siler.
print(sayilar)

isimler.remove('canan')
print(isimler)

# sıralama
sayilar.sort()

sayilar.pop()  # default son değeri siler.
print(sayilar)
sayilar.pop(1)  # default son değeri siler.
print(sayilar)

isimler.remove('Alper')
print(isimler)

sayilar.reverse() # listeyi ters çevirme.

# sayma

sonuc = sayilar.count(5)
print(sonuc)