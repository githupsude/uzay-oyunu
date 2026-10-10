# uzay_oyunu/kayit.py

def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler) -> str:
    """Görev detaylarını biçimlendirilmiş metin olarak döndürür."""
    cikti = [f"[{oncelik.upper()}] {baslik}"]
    for i, adim in enumerate(adimlar, start=1):
        cikti.append(f"  {i}. {adim}")
    for anahtar, deger in ekler.items():
        cikti.append(f"  {anahtar}: {deger}")
    return "\n".join(cikti)

if __name__ == "__main__":
    adim_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_bilgiler = {"sorumlu": "Ayşe"}
    
    # Liste (*) ve Sözlük (**) açarak çağırma örneği
    sonuc = gorev_kaydi("Kara deliğe atla", *adim_listesi, oncelik="YÜKSEK", **ek_bilgiler)
    print(sonuc)