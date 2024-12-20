# Sets | İndexlenemez, Sıralanamaz, Güncellenemez, Elemanlar Tekrarlanamaz, Eleman siler veya ekleriz.

# index olmadığı için pop ile değer verilmeden silinen veriler rastgele olarak silinir.

meyveler = {"elma", "armut", "kiraz"}
meyveler2 = {"elma", "armut", "kiraz","kavun"}

meyveler.add("elma") # değer olduğu için eklenmedi.
meyveler.update(meyveler2) # Meyveler 2 de olan meyveler de olmayan veriler, meyvelere eklenmiştir.

#meyveler.remove("vişne") # değer yoksa hata fırlatır.
meyveler.discard("vişne")




sonuc = meyveler
print(sonuc)