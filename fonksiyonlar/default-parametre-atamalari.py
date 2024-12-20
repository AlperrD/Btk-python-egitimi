def usAlma (taban, us = 2): # us == 2 yapma durumu default parametre yapmaktır. Eğer sonradan değer gönderirsek sonradan gönderdiğimiz değer onu ezer ve gönderdiğimiz değer kullanılır.
    return taban ** us  # Eğer ilk parametre için default değer kullanırsak diğerleri için de kullanmak zorundayız. Ya ikisine de atama yaparız ya da sadece son parametre default olur.

print(usAlma(2,20)) 
