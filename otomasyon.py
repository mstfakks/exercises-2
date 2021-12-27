#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 18:02:01 2021

@author: mustafa
"""

class ogrenciBilgi:
    def __init__(self):
        self.work = True
    def otomasyonTercih (self):
        tercih = self.secim()
        
        if tercih == 1:
            self.ogrenciKayit()
        if tercih == 2:
            self.ogrenciBilgi()
        if tercih == 3:
            self.ogrenciSil()
            
    def secim(self):
        tercih = int(input("Otomasyona Hoşgeldiniz\nÖğreci Bilgi Kayıt için 1'e basınız:\nÖğrenci Bilgi sorgulamak için 2'ye basınız:\nÖğrenci silmek için 3'e basınız:"))
        while tercih<1 or tercih>3:
            tercih = int(input("Hatalı tuşlama yaptınız tekrar deneyiniz: "))
        return tercih
    
    def ogrenciKayit(self):
        isim = input("Öğrenci ismini giriniz: ")
        soyisim = input("Öğrenci soyadını giriniz: ")
        sınıf = input("Sınıfınızı giriniz: ")
        yas = input("Yaşınızı giriniz: ")
        cinsiyet = input("Cinsiyetinizi giriniz: ")
        
        with open("öğrenci.txt","r") as dosya :
            ogrencilist = dosya.readlines()
            if len(ogrencilist)==0:
                no = 1
            else:
                no = (len(ogrencilist)+1)
        with open("öğrenci.txt","a") as dosya:
            dosya.write(str(no)+')' + isim + " "+ soyisim + " " + sınıf + "." + "sınıf" + " " +  "Yaş" + ":" + yas + " " + cinsiyet + "\n")
    def ogrenciBilgi(self):
        o_no = input("Bilgilerini sorgulamak istediğiniz öğrenci numarasını giriniz: ")
        with open("öğrenci.txt","r") as dosya:
            ogrenci_list = dosya.readlines()
        for a in range(len(ogrenci_list)):
            if ogrenci_list[a][0:1] == o_no:
                print(ogrenci_list[a])
    def ogrenciSil(self):
        o_no = input("Silmek istediğiniz öğrencinin numarasını giriniz: ")
        with open("öğrenci.txt","r") as dosya:
            listesil = dosya.readlines()
            for a in range(len(listesil)):
                if listesil[a][0:1] == o_no:
                    listesil.pop(a)
            dosya.close()
        with open("öğrenci.txt","w") as dosya:
            for a in listesil:
                dosya.write(a)
                
ogrenci = ogrenciBilgi()
while ogrenci.work:
    ogrenci.otomasyonTercih()
    
    
    

            
        
        
         