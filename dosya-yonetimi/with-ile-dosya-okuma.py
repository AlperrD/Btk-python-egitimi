# dosya okuma kısmında yaptığımız uzun işlemleri with komutu ile sonrasında close() komutu çağırmadan otomatik olarak bellekten silinmesini sağlayabiliriz.

# with open("deneme.txt", "r") as file: # bu işlemler ile okur ve otomatik olarak bellekten siler.
#     print(file.read())

try: 
    with open("deneme.txt", "r") as file:
        for i in file:
            print(i, end= "") # end ile oluşan alt satır boşluk karakterlerini temizleriz.
except FileNotFoundError as e: # try ile kodu çalıştırıp hata oluştuğunda except ile hatayı kontrol ederiz.
    print("Dosya yolu bulunamadı. ")
