# -*- coding: utf-8 -*-

sozluk = {"ç" : "c",
          "ğ" : "g",
          "ı" : "i",
          "ö" : "o",
          "ş" : "s",
          "ü" : "u",
          "Ç" : "C",
          "Ğ" : "G",
          "İ" : "I",
          "Ö" : "O",
          "Ş" : "S",
          "Ü" : "U"
          }

sonuc = ""
metin_kutusu = input("Metninizi yazın: ")
# metin_kutusu =""" """     # Bu kısma çok satırlı metin yazarak ta kodu çalıştırabilirsiniz.

for harf in metin_kutusu:
    if harf not in sozluk:
        sonuc += harf
    else:
        sonuc += sozluk[harf]

print(sonuc)