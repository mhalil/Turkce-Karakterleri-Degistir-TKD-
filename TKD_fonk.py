def degistir(kelime):
    sonuc = ""
    harfler = { "ç" : "c", "ğ" : "g", "ı" : "i", "ö" : "o", "ş" : "s", "ü" : "u",
                "Ç" : "C", "Ğ" : "G", "İ" : "I", "Ö" : "O", "Ş" : "S", "Ü" : "U"}
    for harf in kelime:
        if harf in harfler.keys():
            sonuc += harfler[harf]
        else:
            sonuc += harf
    return sonuc

veri = input("Metninizi yazın: ")

print(degistir(veri))