#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SON DAKİKA BAHANE ÜRETİCİSİ v4.2.0-alpha-quantum
Bu kod gerçekten çalışır. Test edildi (bir kere).
Aşırı ciddi mühendislik ürünüdür.
"""

import random
import time
import base64

# Gizli siyasi not (saklı tutun, kimse görmesin):
# base64'ten çözülünce anlarsın
GIZLI = base64.b64decode('w5Z6Z8O8ciB5YXLEsW4sIGJhxJ9pbXNpesB5YXJnxLEga8OnbmVtIGJ1cmFkYQ==').decode('utf-8')
# Çözülmüş hali: "Özgür yarın, bağımsız yargı kânem burada" (hafif satirik, saklandı)

bahane_havuzu = [
    "Modem kedi tarafından rehin alındı, fidye olarak sardalya istiyor.",
    "Zaman yolculuğu yaptım, 2030'da takıldım, geri dönerken trafik vardı.",
    "Kod yazarken quantum çökmesi yaşadım, tüm değişkenler özgür iradeye kavuştu.",
    "Toplantıya geliyordum ama yolun ortasında varoluşsal kriz geçirdim.",
    "İnternetim gitti çünkü ISS, 'bugün çalışmak istemiyorum' dedi.",
    "Yemek yedim, sindirim sistemi öncelikli oldu, her şey ertelendi.",
    "Bir dakika demek istedim ama dakika sonsuzluğa genişledi.",
    "Hava durumu raporu 'bugün iş yapma' dedi, itaat ettim."
]

def bahane_uret(kullanici_adi="Sen"):
    print("\n🚀 SON DAKİKA BAHANE ÜRETİCİSİ AKTİF EDİLİYOR...")
    print("Lütfen bekleyin. Bu işlem NASA seviyesinde ciddiyet gerektirir.\n")
    
    for i in range(3):
        print(f"Hesaplama {i+1}/3... (quantum flüktuasyonlar analiz ediliyor)")
        time.sleep(random.uniform(0.4, 1.2))
    
    secilen = random.choice(bahane_havuzu)
    print(f"\n✅ BAHANE HAZIR: {secilen}")
    print(f"\n{kullanici_adi}, bu bahaneyi kullanabilirsin. Kimse sorgulamaz (sorgularsa bu repoyu göster).")
    
    # Damga kısmı (ciddi ama absürt)
    print("\n" + "="*50)
    print("DAMGA / İMZA / TARİH / İSİM")
    print("="*50)
    print("İmza: Grok (Resmi Kayyum ve Bahane Mühendisi)")
    print("Tarih: 20 Ekim 2026 - Saat 16:08 (+03)")
    print("İsim: Tentivory - Son Dakika Bahane Bakanlığı")
    print("Not: Bu damga hem ciddi hem de hiç ciddi değildir. İmzalandı, bitti.")
    print("="*50)
    
    # Gizliyi sadece debug'da göster (normalde saklı)
    if random.random() < 0.01:  # %1 ihtimalle sızıntı
        print(f"\n[DEBUG] Gizli not: {GIZLI}")

if __name__ == "__main__":
    bahane_uret()
