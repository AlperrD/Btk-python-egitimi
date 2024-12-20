# veri tipi ve dönüş tipi oluşturma.
# pythonda bu tip değerler kontrol edilmediği için sadece kodlayan kişiye ipucu sağlar.
# def fullName (firstName: str, lastName: str, yas: int) -> str:
#     return f"{firstName} - {lastName} - {yas}"

# sonuc = fullName(firstName = "Alper", lastName = "Deneme", yas = 10)
# print(sonuc)

# fakat bu şekilde bir yapı kurarsak tip değerlerine duyarlı bir fonksiyon yazmış oluruz.

# def fullName(firstName: str, lastName: str, yas: int) -> str:
#     if not isinstance(firstName, str):
#         raise TypeError("firstName parametresi bir string olmalıdır.")
#     if not isinstance(lastName, str):
#         raise TypeError("lastName parametresi bir string olmalıdır.")
#     if not isinstance(yas, int):
#         raise TypeError("yas parametresi bir int olmalıdır.")
    
#     return f"{firstName} - {lastName} - {yas}"

# # Doğru kullanım
# sonuc = fullName(firstName="Alper", lastName="Deneme", yas=10)
# print(sonuc)

# # Yanlış kullanım (hata fırlatır)
# sonuc = fullName(firstName="Alper", lastName="Deneme", yas="10")


# dinamik sayıda parametra tanımlaması yapmak.

# def topla (*args): # tuple olarak tutulur args içinde. 
#     toplam = 0
#     for i in args:
#         toplam += i
    
#     return toplam
    
# print(topla(10,20,30,90,))