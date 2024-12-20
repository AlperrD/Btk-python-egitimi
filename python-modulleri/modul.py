# liste tanımlama
from termcolor import colored
liste = [
    {"Ali": "30"},
    {"Veli": "40"}
]

# öğe ekleme fonksiyonu
def ogeEkle(ad, puan):
    item = {ad: puan}
    liste.append(item)

# öğe listeleme fonksiyonu
def ogeListele():
    for i in liste:
        print(colored(i, color="white", on_color="on_yellow"))  # Use print to display all items
