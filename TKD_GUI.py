# -*- coding: utf-8 -*-

import tkinter as tk
import pyperclip

# Pencere Ebatları ve Renk Tanımları
pencere = tk.Tk()

arkaplan_rengi = "#93ac93"
arkaplan_rengi_metin = "#b7c8b7"
arkaplan_rengi_buton = "white"

pencere.geometry("500x500+500+350")
pencere.resizable("FALSE", "FALSE")
pencere.title("Türkçe Karakterleri Değiştir (TKD)")
pencere.configure(bg = arkaplan_rengi)

# TÜRKÇE karakterlerin değiştirileceği karakterleri tanımlayan sözlük (dict) yapısı
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

def degistir():
    sonuc = ""
    for harf in girdi_penceresi.get("1.0", "end"):
        if harf not in sozluk:
            sonuc += harf
        else:
            sonuc += sozluk[harf]
    sonuc_penceresi.insert(tk.END,sonuc + "\n")

def temizle():
    girdi_penceresi.delete("1.0",tk.END)
    sonuc_penceresi.delete("1.0",tk.END)

def kopyala():
    deger = sonuc_penceresi.get("1.0", "end").strip()
    pyperclip.copy(deger)
    
girdi_penceresi = tk.Text(pencere,
                width=59,
                height=10,
                state="normal")
girdi_penceresi.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

sonuc_penceresi = tk.Text(pencere,
                width=59,
                height=10,
                state="normal")
sonuc_penceresi.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

btn_sil = tk.Button(pencere,
                    text = "Temizle",
                    width = 10,
                    height=2,
                    font = "Tahoma,Calibri,Verdana,DejaVuSans,LiberationSans,Ubuntu 10 bold",
                    bg = arkaplan_rengi_buton,
                    fg = "black",
                    command= temizle)
btn_sil.grid(row=3, column=0, padx=0, pady=5)

btn_degistir = tk.Button(pencere,
                    text = "Değiştir",
                    width = 10,
                    height=2,
                    font = "Tahoma,Calibri,Verdana,DejaVuSans,LiberationSans,Ubuntu 10 bold",
                    bg = arkaplan_rengi_buton,
                    fg = "black",
                    command= degistir)
btn_degistir.grid(row=3, column=1, padx=0, pady=5)

btn_sil = tk.Button(pencere,
                    text = "Kopyala",
                    width = 10,
                    height=2,
                    font = "Tahoma,Calibri,Verdana,DejaVuSans,LiberationSans,Ubuntu 10 bold",
                    bg = arkaplan_rengi_buton,
                    fg = "black",
                    command= kopyala)
btn_sil.grid(row=4, column=0, padx=0, pady=5)

btn_degistir = tk.Button(pencere,
                    text = "Kapat",
                    width = 10,
                    height=2,
                    font = "Tahoma,Calibri,Verdana,DejaVuSans,LiberationSans,Ubuntu 10 bold",
                    bg = "#A02C2C",
                    fg = "white",
                    command= quit)
btn_degistir.grid(row=4, column=1, padx=0, pady=5)

pencere.mainloop()