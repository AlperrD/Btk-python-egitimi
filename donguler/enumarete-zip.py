# enumerate yapısı.

markalar = ["opel", "bmw", "togg"]

obj1 = enumerate(markalar, 1)

print(type(obj1))
print(list(obj1))

for index, marka in enumerate(markalar,1):
    print(f"{index} - {marka}")


#Zip Liste birleştirme. 

numara = [100,200,300]
ogrenci = ["Ali" , "Ayşe", "Zeynep"]

print(list(zip(numara,ogrenci)))

for ogr in zip(numara, ogrenci):
    print(ogr)

for no, isim in zip(numara, ogrenci):
    print(f"{no} - {isim}")