# "w" modunda aç
# dosya konumda oluşturulur.
# eğer konumda aynı dosya varsa dosya silinir ve yeni oluşturulur.

file = open ("dosya.txt" , "w")

file.write("Alper Deneme\n ") # write işlemi veri kaybına yol açar eski dosya içeriğini siler ve yeni dosya ile günceller !!

file.close()