customers = ["sadikturan", "mehmetyilmaz", "ahmetyilmaz", "pekindegirmenci"]
order_details = [12000,2000,1300,15000]

# sadikturan kullanici adı ile yapılan siparişi listeye ekleyiniz.

customers.append("sadikturan")
order_details.append(5000)

sonuc = customers

# son eklenen siparişi siliniz.

customers.pop()
order_details.pop() # index ile silme işlemleri

sonuc = customers

# tüm müşteriler için sipariş listesini yazdırın. (Döngüler ile sonraki kısımlarda yapılacak.)

a = f'{customers[0]} adlı müşterinin sipariş tutarı: {order_details[0]} dir.'
b = f'{customers[1]} adlı müşterinin sipariş tutarı: {order_details[1]} dir.'

print(a,b)

# müşterileri alfabetik olarak sıralayınız.

sonuc = customers.sort()
print(customers) # sort metodu geriye değer döndürmez.

# en düşük sipariş hangisidir.

sonuc = min(order_details)

# sadikturanin kaç tane siparişi vardır.

sonuc = customers.count('sadikturan')

# ahmetyilmaz adlı kullanıcıyı sil

sonuc = customers.remove('ahmetyilmaz') # siler ve geriye değer döndürmez // pop ise sondan eleman siler.
# pop index ile siler remove ise içine girilen değere göre siler (str)
print(customers)

# kullanıcıdan alınan isim ve değeri ilgili listelere ekle.
userName = ''
deger = 0

userName = input('bir kullanıcı adı giriniz.')
deger = input('Ne kadar harcama yaptığını giriniz.')

customers.append(userName)
order_details.append(int(deger))

print(customers)
print(order_details)








print(sonuc)