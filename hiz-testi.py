import speedtest

def speed_test():
    st = speedtest.Speedtest()

    print("Sunucular belirleniyor...")
    st.get_best_server()

    print("İnternet hızı testi başlatılıyor...")
    download_speed = st.download() / 1_000_000  # Mbps cinsine çevir
    upload_speed = st.upload() / 1_000_000  # Mbps cinsine çevir
    ping = st.results.ping

    print(f"İndirme Hızı: {download_speed:.2f} Mbps")
    print(f"Yükleme Hızı: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")

if __name__ == "__main__":
    speed_test()
