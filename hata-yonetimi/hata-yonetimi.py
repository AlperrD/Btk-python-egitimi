while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))

        print(x/y)
    except ZeroDivisionError as e:
        print("Y sıfır olamaz.")
        print(e)
    except ValueError as e:
        print("X ve Y değerleri sayısal değer olmalıdır.")
        print(e)
    except Exception as e:
        print(f"Bilinmeyen bir hata oluştu. {e}")
    else:  # try except bloklarının else kısmı da vardır bu şekilde hata oluşmadıysa sorunsuz çalıştığı durumda döngüden çıkmak için kullanılabilir.
        break
    finally:
        print("Finally bloğu çalıştı") # her halükarda çalışacak olan bir bloktur.