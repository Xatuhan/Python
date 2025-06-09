# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 19:38:58 2025
"""

import sqlite3

def veritabani_baglan():
    conn = sqlite3.connect('banka_proje.db')
    return conn

def tablo_olustur():
    conn = veritabani_baglan()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS kullanicilar (
            tc INTEGER PRIMARY KEY,
            ad TEXT,
            soyad TEXT,
            yas INTEGER,
            tel TEXT,
            eposta TEXT,
            sifre TEXT,
            bakiye REAL,
            iban TEXT
        )
    ''')
    conn.commit()
    conn.close()

tablo_olustur()

sabit_islem_ucreti=(2.56)
kisiler={}
yonetici_sozluk={}
yonetici_liste=[]
tum_islemler={}

class Kullanici:
    def __init__(self, ad, soyad, tc, yas, tel, eposta, sifre, bakiye=0, iban=None):
        self.ad = ad
        self.soyad = soyad
        self.tc = tc
        self.yas = yas
        self.tel = tel
        self.eposta = eposta
        self.sifre = sifre
        self.bakiye = bakiye
        self.iban = iban
        self.islem_gecmisi = []

    def __str__(self):
        return f"Ad: {self.ad} {self.soyad}, TC: {self.tc}, Yaş: {self.yas}, Tel: {self.tel}, E-posta: {self.eposta}, Bakiye: {self.bakiye} TL, IBAN: {self.iban}"

class Yonetici:
    def __init__(self, kullanici_adi, sifre):
        self.kullanici_adi = kullanici_adi
        self.sifre = sifre

    def __str__(self):
        return f"Yönetici: {self.kullanici_adi}"

def kredi_uygunluk_hesaplama(x1,x2,x3):
    dti_fonk= int(x1) / int(x2) / int(x3) * 100
    return dti_fonk
def admin_giris(kisiler, yonetici_sozluk, tum_islemler):
    while True:
        adminadsoru = input("KULLANICI İSMİNİZİ GİRİNİZ \n")
        adminsifresoru = input("Parola giriniz:")
        if (adminadsoru == "ADMIN" and adminsifresoru == "ADMIN"):
            print("Hosgeldin ADMIN\n")
            break
        else:
            print("Yanlış tuşlara bastınız, lütfen tekrar deneyin.")
            continue
    while True:
        islem_sorgusu = input("""Hangi işlemi yapmak istersiniz?
        1- Kullanıcı Taleplerine Erişim
        2- Kullanıcı işlem Geçmişlerine Bak
        3- Kullanıcı Bilgileri
        4- Çıkış""")
        if (islem_sorgusu == "1"):
            while True:
                talep_sor = input("""Kullanıcı Taleplerine Erişim Sekmesine Hoşgeldiniz. 
                Talepleri görmek için 1 , sekmeden çıkmak için 2 ye basınız.""")
                if (talep_sor == "1"):
                    if not yonetici_sozluk:
                        print("Hiçbir talep bulunadı.")
                    for i in yonetici_sozluk.keys():
                        print(yonetici_sozluk[i])
                    continue
                if (talep_sor == "2"):
                    print("Sekmeden çıkış yapılıyor")
                    break
        if (islem_sorgusu == "2"):
            while True:
                sor_islem_gecmisi = input("""Kullanıcı bilgilerine erişmek istiyorsanız "Evet", çıkış için "Kapat" yazınız""")
                if not tum_islemler:
                    print("Hiçbir kullanıcı işlemi yok.")
                if sor_islem_gecmisi.lower() == "evet":
                    print(tum_islemler)
                elif sor_islem_gecmisi.lower() == "kapat":
                    print("Kapatılıyor")
                    break
        if (islem_sorgusu == "3"):
            while True:
                bilgi_sor = input("""Kullanıcı bilgilerine erişmek istiyorsanız "Evet", çıkış için "Kapat" yazınız""")
                if not kisiler:
                    print("Kullanıcı yok")
                if (bilgi_sor.lower() == "evet"):
                    for tc, kullanici in kisiler.items():
                        print(kullanici)
                if (bilgi_sor.lower()) == "kapat":
                    print("Sekmeden çıkış yapılıyor")
                    break
        if (islem_sorgusu == "4"):
            print("Çıkış yapılıyor")
            break
        else:
            print("ÖNCEKİ SEKMEYE DÖNÜLÜYOR. ")
            continue



def kullanici_giris():
    while True:
        print("\nHoşgeldiniz\n")
        ad = input("\nAdınızı giriniz:")
        soyad = input("\nSoyadınızı giriniz:")
        tam_isim = ad[0:1:1].upper() + ad[1:].lower() + " " + soyad[0:1:1].upper() + soyad[1::].lower()
        try:
            tc = int(input("\nTC GİR:"))
        except:
            print("Sadece sayı gir.")
            tc = int(input("\nTC GİR:"))
        while True:
            try:
                yas = int(input("\nYas GİR:"))
                if yas < 18 or yas > 140:
                    print("Lütfen geçerli bir yaş giriniz.")
                    continue
                else:
                    break
            except:
                print("Sadece sayı gir.")
        while True:
            try:
                tel = int(input("\nLütfen telefon numaranızı 0 olmadan giriniz :"))
                if len(str(tel)) == 10:
                    break
                else:
                    print("Lütfen doğru şekilde tuşlama yapınız.")
                    continue
            except:
                print("Sadece sayı gir.")
        bakiye = 0
        while True:
            epostadeneme = input("\nEpostanızı giriniz:")
            sifre = input("\nSifre olustur\n")
            eposta = input("\nE postanızı tekrar gir\n")
            sifre2 = input("\nSifrenizi tekrar giriniz\n")
            if (epostadeneme == eposta and sifre == sifre2):
                sayi = ''.join([str(__import__('random').randint(0, 9)) for _ in range(24)])
                iban = "TR" + str(sayi)
                kullanici = Kullanici(ad, soyad, tc, yas, tel, eposta, sifre2, bakiye, iban)
                kisiler.setdefault(tc, kullanici)
                # Veritabanına ekle
                conn = veritabani_baglan()
                cursor = conn.cursor()
                cursor.execute('''INSERT OR REPLACE INTO kullanicilar (tc, ad, soyad, yas, tel, eposta, sifre, bakiye, iban) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                               (tc, ad, soyad, yas, str(tel), eposta, sifre2, bakiye, iban))
                conn.commit()
                conn.close()
                print("Sayın", kullanici.ad, kullanici.soyad, "bankamıza hoşgeldiniz :D \n")
                print("Sayın", kullanici.ad, kullanici.soyad, "IBAN ınız: ", kullanici.iban)
                return kisiler, kullanici, tc
            else:
                print("Şifrenizi veya kullanıcı adınızı yanlış girdiniz. Tekrar deneyin")
                continue

def islem_gecmisi_dosyaya_yaz(tc, islem):
    dosya_adi = f"islem_gecmisi_{tc}.txt"
    with open(dosya_adi, "a", encoding="utf-8") as f:
        f.write(str(islem) + "\n")

def islem_gecmisi_goster(tc):
    dosya_adi = f"islem_gecmisi_{tc}.txt"
    f = open(dosya_adi, "r", encoding="utf-8")
    print("\n--- İşlem Geçmişiniz ---")
    for satir in f:
        print(satir.strip())
    print("-----------------------\n")
    f.close()

def main():
    while True:
        secim = input("1-Kullanıcı girişi\n2-Admin girişi\n3-Çıkış\n")
        if (secim == "1"):
            kisiler, kullanici, tc = kullanici_giris()
            islem_gecmisi = []
            while True:
                kullanici_islemleri=input("""
            1-Para Çekme
            2-Para Yatırma
            3-Para Gönderme
            4-Kredi Başvurusu
            5-Yetkiliye Talep Gönderme
            6-İşlem Geçmişini Göster
            7-Çıkış
                """)
                if(int(kullanici_islemleri))==1:
                    cekilen_para=input("Lütfen çekmek istediğiniz para miktarını tuşlayınız")
                    if int(cekilen_para)<=0:
                        print("Lütfen pozitif bir değer giriniz.")
                        continue
                    if (kisiler[tc].bakiye<int(cekilen_para)):
                        print("Bakiyeniz yetersiz lütfen önce para yatırın.")
                        continue
                    elif (kisiler[tc].bakiye >= int(cekilen_para)):
                        onceki_bakiye1=kisiler[tc].bakiye
                        kisiler[tc].bakiye-=int(cekilen_para)
                        islem_paracekme=("Para çekme:" ,onceki_bakiye1," TL  önceki bakiye -----> islem sonrası bakiye",kisiler[tc].bakiye,"TL")
                        islem_gecmisi.append(islem_paracekme)
                        islem_gecmisi_dosyaya_yaz(tc, islem_paracekme)
                        print("Sayın", kisiler[tc].ad, kisiler[tc].soyad, "Güncel bakiyeniz: ", kisiler[tc].bakiye, "TL")
                        continue
                    else:
                        print("Hatalı tuşlama yaptınız. Tekrar deneyin.")
                        continue
                elif(int(kullanici_islemleri))==2:
                    yatirilan_para=input("Lütfen yatırmak istediğiniz para miktarını giriniz:")
                    if int(yatirilan_para)<=0:
                        print("Hatalı değer girdiniz, girdiğiniz değer pozitif olmalı.")
                        continue
                    elif int(yatirilan_para)>=0:
                        onceki_bakiye2 = kisiler[tc].bakiye
                        kisiler[tc].bakiye+=int(yatirilan_para)
                        islem_parayatirma=("Para Yatırma:" ,onceki_bakiye2," TL  önceki bakiye -----> islem sonrası bakiye",kisiler[tc].bakiye,"TL")
                        islem_gecmisi.append(islem_parayatirma)
                        islem_gecmisi_dosyaya_yaz(tc, islem_parayatirma)
                        print("Sayın",kisiler[tc].ad, kisiler[tc].soyad,"Güncel bakiyeniz: ",kisiler[tc].bakiye,"TL")
                        continue
                    else:
                        print("Hatalı tuşlama yaptınız tekrar deneyin.")
                elif int(kullanici_islemleri) == 3:
                    gonderilen_iban = input("Para göndermek istediğiniz hesabın IBAN numarasını giriniz: ")
                    alici_bulundu = False
                    for tc_key, bilgiler in kisiler.items():
                        if bilgiler.iban == gonderilen_iban and tc_key != tc:
                            alici_tc = tc_key
                            alici_bulundu = True
                            break
                    if not alici_bulundu:
                        print("Bu IBAN numarası sistemde kayıtlı değil veya kendinize para gönderemezsiniz.")
                        continue
                    try:
                        gonderilen_para = float(input("Göndermek istediğiniz miktarı giriniz: "))
                        if gonderilen_para <= 0:
                            print("Lütfen geçerli bir miktar giriniz.")
                            continue
                    except:
                        print("Hatalı giriş yaptınız.")
                        continue

                    toplam_tutar = gonderilen_para + sabit_islem_ucreti
                    if kisiler[tc].bakiye < toplam_tutar:
                        print("Bakiyeniz yetersiz.")
                        continue
                    print(f"""Sayın {kisiler[tc].ad} {kisiler[tc].soyad}, {kisiler[tc].iban} IBAN'dan
                    {gonderilen_iban} IBAN'ına {gonderilen_para} TL göndermek üzeresiniz.
                    İşlem ücreti: {sabit_islem_ucreti} TL.
                    Toplam düşecek bakiye: {toplam_tutar} TL
                    ONAYLIYOR MUSUNUZ?""")
                    onay = input("evet/hayir? ")
                    if onay.lower() =="evet":
                        
                        onceki_bakiye_gonderici =kisiler[tc].bakiye
                        kisiler[tc].bakiye-=toplam_tutar
                        
                        onceki_bakiye_alici = kisiler[alici_tc].bakiye
                        
                        kisiler[alici_tc].bakiye += gonderilen_para
                        islem_gecmisi.append(
                            f"Gönderdiğiniz kişi: {kisiler[alici_tc].ad} - IBAN: {gonderilen_iban} - Miktar: {gonderilen_para} TL - Önceki bakiye: {onceki_bakiye_gonderici} TL -> Yeni bakiye: {kisiler[tc].bakiye} TL")
                        islem_gecmisi_dosyaya_yaz(tc, f"Gönderdiğiniz kişi: {kisiler[alici_tc].ad} - IBAN: {gonderilen_iban} - Miktar: {gonderilen_para} TL - Önceki bakiye: {onceki_bakiye_gonderici} TL -> Yeni bakiye: {kisiler[tc].bakiye} TL")
                        print("İşlem başarılı. Güncel bakiyeniz:", kisiler[tc].bakiye, "TL")
                    else:
                        print("İşlem iptal edildi.")
                    continue
                elif(int(kullanici_islemleri))==4:
                    while True:
                        try:
                            aylik_gelir=int(input("Lütfen aylık gelirinizi giriniz."))
                            if aylik_gelir>=0:
                                break
                            else:
                                print("Negatif değer girilemez")
                                continue
                        except :
                            print("Düzgün tuşlara bas.")
                            continue
                    while True:
                        try:
                            kredi_istek_miktar=int(input("Lütfen almak istediğiniz kredi miktarını giriniz."))
                            if kredi_istek_miktar>=0:
                                break
                            else:
                                print("Negatif değer girilemez")
                                continue
                        except:
                            print("Düzgün tuşlara bas.")
                            continue
                    while True:
                        try:
                            zaman=int(input("Kaç aylık sürede kredinizi ödemek istersiniz?"))
                            if zaman>=0:
                                break
                            else:
                                print("Negatif değer girilemez")
                        except :
                            print("Düzgün tuşlara bas.")
                            continue
                    dti=kredi_uygunluk_hesaplama(kredi_istek_miktar,zaman,aylik_gelir)
                    kredi_tipi = input("""Almak istediğiniz kredi türünü eksiksiz tuşlayınız.
                                        1-İhtiyaç Kredisi
                                        2-Konut kredisi
                                        3-Taşıt kredisi
                                        """)
                    if kredi_tipi=="1":
                        if int(kredi_istek_miktar)<=200000:
                            print("Girdiğiniz miktar kredi için uygun")
                            if dti<=40:
                                print("İhtiyaç kredisi alabilirsiniz")
                            else:
                                print("Maalesef net geliriniz yeterliliği karşılamıyor.")
                        else:
                            print("Girdiğiniz kredi miktarı ihtiyaç kredisi için fazla")
                    elif kredi_tipi=="2":
                        if int(kredi_istek_miktar)>=1000000 and int(kredi_istek_miktar)<16000000:
                            print("Girdiğiniz miktar kredi için uygun")
                            if dti<=40:
                                print("İhtiyaç kredisi alabilirsiniz")
                            else:
                                print("Maalesef net geliriniz yeterliliği karşılamıyor.")
                        else:
                            print("Girdiğiniz kredi miktarı konut kredisi için fazla")
                    elif kredi_tipi=="3":
                        if int(kredi_istek_miktar)>=200000 and (kredi_istek_miktar)<=5000000:
                            print("Girdiğiniz miktar kredi için uygun")
                            if dti<=40:
                                print("İhtiyaç kredisi alabilirsiniz")
                            else:
                                print("Maalesef net geliriniz yeterliliği karşılamıyor.")
                        else:
                            print("Girdiğiniz kredi miktarı ihtiyaç kredisi için fazla")
                    else:
                        print("Hatalı tuşlama yaptınız")
                elif int(kullanici_islemleri)==5:
                    while True:
                        mesaj=input("Yetkililere iletmek istediğiniz öneri/şikayetinizi giriniz:")
                        talep=("Kimden:",kisiler[tc].ad, kisiler[tc].soyad,"Gönderen E-posta Adresi:",kisiler[tc].eposta,"İleti: ",mesaj)
                        print("Kimden:",kisiler[tc].ad, kisiler[tc].soyad,"Gönderen E-posta Adresi:",kisiler[tc].eposta,"İleti: ",mesaj)
                        yonetici_liste.append(talep)
                        yonetici_sozluk.setdefault(tc,yonetici_liste)
                        print("Talebiniz bankamıza iletilmiştir.")
                        cikis_sor=input("Çıkış yapmak ister misiniz? E/H")
                        if(cikis_sor.lower()=="e"):
                            print("Çıkış yaptınız.")
                            break
                        elif(cikis_sor.lower()=="h"):
                            print("Devam edilecek.")
                            continue
                        else:
                            print("Hatalı tuşlara bastınız, program sonlandırılıyor")
                            continue
                elif int(kullanici_islemleri)==6:
                    islem_gecmisi_goster(tc)
                elif(int(kullanici_islemleri))==7:
                    tum_islemler[tc]=islem_gecmisi
                    print("Programdan çıktınız\n")
                    break
                else:
                    print("Hatalı tuşlara bastınız. Tekrar deneyin")
                    continue
        elif(secim=="2"):
            admin_giris(kisiler, yonetici_sozluk, tum_islemler)
        elif(secim=="3"):
            print("Programdan çıktınız\n")
            break
        else:
            print("HATALI SEÇİM! TEKRAR DENEYİN")
            continue
main()
