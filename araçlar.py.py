# uzay_oyunu/araclar.py

def hamle_sayaci():
    """Her çağrıldığında artan bir sayaç döndüren closure fonksiyonu."""
    sayac = 0
    def arttir():
        nonlocal sayac
        sayac += 1
        return sayac
    return arttir

def en_bagli_gezegenler(galaksi: dict) -> list:
    """Gezegenleri bağlantı sayısına göre azalan, eşitlikte alfabetik sırada döndürür."""
    baglantilar = galaksi.get("baglantilar", {})
    return sorted(baglantilar.keys(), key=lambda g: (-len(baglantilar[g]), g))