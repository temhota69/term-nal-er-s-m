import os

cls = lambda: os.system('cls' if os.name == 'nt' else 'clear')

while True:
    cls()
    print("--- GELİŞMİŞ HESAPLAYICI ---")
    denklem = input("\nDenklemi yazın (Çıkış için 'q'): ")

    if denklem.lower() == 'q':
        break

    try:
        # Python'da (3+1)5 yazımı hatadır, (3+1)*5 olması gerekir.
        # Bu satır, parantezden sonra sayı gelirse araya çarpı (*) koyar.
        denklem = denklem.replace(")(", ")*(").replace(") ", ")*")
        
        # eval() fonksiyonu metni alır ve matematiksel olarak hesaplar
        sonuc = eval(denklem)
        
        print(f"\nİşlem: {denklem}")
        print(f"Sonuç: {sonuc}")
        
    except Exception as e:
        print(f"\nHata: Yazım yanlış olabilir! ({e})")

    input("\nDevam etmek için Enter...")