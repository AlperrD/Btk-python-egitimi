# global değer ve local değer örnekleri

x = 100 # global kapsam.

def degistir (x):
    #x = 20 # local kapsam
    print(x)
degistir(50) # dışarıdan parametre gönderirsek ise pass by value olarak gönderilir. Globaldeki kapsam etkilenmez.
print(x)

# global kapsamdaki değeri değiştirme

def globalDegistir():
    global x
    x = 3000
    print(x)

globalDegistir()
print(x)

# sonuç olarak pass by reference yapmak için global keywordünü kullanırız.