import pandas as pd

# Dosya yolunu belirtin
file_path = "dosya.xls"

# Excel dosyasını yükle
df = pd.read_excel(file_path)

# Quiz ortalamasının %25'ini ve final sınavının %30'unu hesaplayarak toplam puanı ekle
df["Quiz Ortalaması"] = (df["Quiz1"] + df["Quiz2"] + df["Quiz3"]) / 3
df["Toplam Puan"] = (df["Quiz Ortalaması"] * 0.25) + (df["Final"] * 0.30)

# Büyükten küçüğe sıralama
df_sorted = df.sort_values(by="Toplam Puan", ascending=False)

# Sonuçları ekrana yazdır
for index, row in df_sorted.iterrows():
    print(f"Ad Soyad: {row['Ad']}, Üniversite: {row['Uni']}, Toplam Puan: {row['Toplam Puan']:.2f}")

# Sıralanmış sonuçları yeni bir Excel dosyasına kaydet
df_sorted.to_excel("Siralama_Sonuc.xlsx", index=False)
