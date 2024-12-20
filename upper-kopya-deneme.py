a = 'Basit bir metin'

upperList = {
    97: 65, 98: 66, 99: 67, 100: 68, 101: 69, 102: 70,
    103: 71, 104: 72, 105: 73, 106: 74, 107: 75, 108: 76,
    109: 77, 110: 78, 111: 79, 112: 80, 113: 81, 114: 82,
    115: 83, 116: 84, 117: 85, 118: 86, 119: 87, 120: 88,
    121: 89, 122: 90
}
reversedUpperList = {v:k for k , v in upperList.items()}

def kucult(a):
    b = ''  # b'yi işlev içinde tanımlıyoruz
    for i in a:
        c = reversedUpperList.get(ord(i), ord(i))  # ASCII değerini alıyoruz ve yoksa varsayılan olarak kendisini alıyoruz
        d = chr(c)  # ASCII kodunu karaktere çeviriyoruz
        b += d  # b string'ine ekliyoruz
    print(b)
    return b

def upperr(a):
    b = ''  # b'yi işlev içinde tanımlıyoruz
    for i in a:
        c = upperList.get(ord(i), ord(i))  # ASCII değerini alıyoruz ve yoksa varsayılan olarak kendisini alıyoruz
        d = chr(c)  # ASCII kodunu karaktere çeviriyoruz
        b += d  # b string'ine ekliyoruz
    print(b)
    return b

upperr('deneme deNeme')
kucult('DNEME DENEME')

c = upperr('Benim adım deneme ')
print(c)
