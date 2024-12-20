liste = [1,2,3,4]

for i in range(1,100,2): # liste oluşturma işlevini görür.
    print(i)

rng= range(1,10) # Listeye dönüştürülebilen obje döner. (başlangıç, bitiş, kaçar kaçar artsın.)

sonuc= list(rng)
print(sonuc)

for i in range(50, 200,1):
    if(i%2 == 0):
        print(i)