def renklendir (metin, renk):
    renkler = ("blue", "red", "yellow", "black")

    if type(metin) is not str:
        raise TypeError("Metin str tipinde olmalıdır.")
    if type(renk) is not str:
        raise TypeError("Renk str tipinde olmalıdır.")
    if renk not in renkler:
        raise ValueError("Geçersiz bir renk") 
    
    print(f"{metin} - {renk} renginde yazıldı.")

try:
    renklendir("Alper", "red")
    renklendir(20, "blue")
    renklendir("deneme" ,"orange")
except (TypeError,ValueError) as e:
    print(e) 