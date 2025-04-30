from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
import threading
import uuid

# Predefined list of valid keys (in a real system, these would be stored securely)
VALID_KEYS = {
    "KEY123-4567-8901": True,
    "KEY987-6543-2109": True,
    "KEY555-1111-9999": True
}

def validate_key(key):
    return key in VALID_KEYS and VALID_KEYS[key]

def key_system():
    system("cls||clear")
    print(Fore.LIGHTCYAN_EX + "\n=== SMS Gönderici - Key Sistemi ===")
    print(Fore.LIGHTYELLOW_EX + "\nLütfen erişim anahtarınızı giriniz: " + Fore.LIGHTGREEN_EX, end="")
    entered_key = input().strip()
    
    if validate_key(entered_key):
        print(Fore.LIGHTGREEN_EX + "\nAnahtar doğrulandı! Sisteme erişiliyor...")
        sleep(2)
        return True
    else:
        print(Fore.LIGHTRED_EX + "\nGeçersiz anahtar! Erişim reddedildi.")
        sleep(3)
        return False

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

# Main program with key check
if key_system():
    while 1:
        system("cls||clear")
        print("""{}

        
        Sms: {}           {}by {}@tingirifistik\n  
        """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))
        try:
            menu = (input(Fore.LIGHTMAGENTA_EX + " 1- SMS Gönder (Normal)\n\n 2- SMS Gönder (Turbo)\n\n 3- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
            if menu == "":
                continue
            menu = int(menu) 
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.")
            sleep(3)
            continue
        if menu == 1:
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız): "+ Fore.LIGHTGREEN_EX, end="")
            tel_no = input()
            tel_liste = []
            if tel_no == "":
                system("cls||clear")
                print(Fore.LIGHTYELLOW_EX + "Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: "+ Fore.LIGHTGREEN_EX, end="")
                dizin = input()
                try:
                    with open(dizin, "r", encoding="utf-8") as f:
                        for i in f.read().strip().split("\n"):
                            if len(i) == 10:
                                tel_liste.append(i)
                    sonsuz = ""
                except FileNotFoundError:
                    system("cls||clear")
                    print(Fore.LIGHTRED_EX + "Hatalı dosya dizini. Tekrar deneyiniz.")
                    sleep(3)
                    continue
            else:
                try:
                    int(tel_no)
                    if len(tel_no) != 10:
                        raise ValueError
                    tel_liste.append(tel_no)
                    sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
                except ValueError:
                    system("cls||clear")
                    print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
                    sleep(3)
                    continue
            system("cls||clear")
            try:
                print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
                mail = input()
                if ("@" not in mail or ".com" not in mail) and mail != "":
                    raise
            except:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
                sleep(3)
                continue
            system("cls||clear")
            try:
                print(Fore.LIGHTYELLOW_EX + f"Kaç adet SMS göndermek istiyorsun {sonsuz}: "+ Fore.LIGHTGREEN_EX, end="")
                kere = input()
                if kere:
                    kere = int(kere)
                else:
                    kere = None
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
                sleep(3)
                continue
            system("cls||clear")
            try:
                print(Fore.LIGHTYELLOW_EX + "Kaç saniye aralıkla göndermek istiyorsun: "+ Fore.LIGHTGREEN_EX, end="")
                aralik = int(input())
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı giriş yaptın. Tekrar deneyiniz.") 
                sleep(3)
                continue
            system("cls||clear")
            if kere is None: 
                sms = SendSms(tel_no, mail)
                while True:
                    for attribute in dir(SendSms):
                        attribute_value = getattr(SendSms, attribute)
                        if callable(attribute_value):
                            if attribute.startswith('__') == False:
                                exec("sms."+attribute+"()")
                                sleep(aralik)
            for i in tel_liste:
                sms = SendSms(i, mail)
                if isinstance(kere, int):
                        while sms.adet < kere:
                            for attribute in dir(SendSms):
                                attribute_value = getattr(SendSms, attribute)
                                if callable(attribute_value):
                                    if attribute.startswith('__') == False:
                                        if sms.adet == kere:
                                            break
                                        exec("sms."+attribute+"()")
                                        sleep(aralik)
            print(Fore.LIGHTRED_EX + "\nMenüye dönmek için 'enter' tuşuna basınız..")
            input()
        elif menu == 3:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Çıkış yapılıyor...")
            break
        elif menu == 2:
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Telefon numarasını başında '+90' olmadan yazınız: "+ Fore.LIGHTGREEN_EX, end="")
            tel_no = input()
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı telefon numarası. Tekrar deneyiniz.") 
                sleep(3)
                continue
            system("cls||clear")
            try:
                print(Fore.LIGHTYELLOW_EX + "Mail adresi (Bilmiyorsanız 'enter' tuşuna basın): "+ Fore.LIGHTGREEN_EX, end="")
                mail = input()
                if ("@" not in mail or ".com" not in mail) and mail != "":
                    raise
            except:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı mail adresi. Tekrar deneyiniz.") 
                sleep(3)
                continue
            system("cls||clear")
            send_sms = SendSms(tel_no, mail)
            dur = threading.Event()
            def Turbo():
                while not dur.is_set():
                    thread = []
                    for fonk in servisler_sms:
                        t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                        thread.append(t)
                        t.start()
                    for t in thread:
                        t.join()
            try:
                Turbo()
            except KeyboardInterrupt:
                dur.set()
                system("cls||clear")
                print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
                sleep(2)
else:
    system("cls||clear")
    print(Fore.LIGHTRED_EX + "Program sonlandırılıyor...")
    sleep(2)