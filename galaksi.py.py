# uzay_oyunu/galaksi.py
import json

def galaksi_kur(gezegenler: list, baglantilar: dict, baslangic: str, **kwargs) -> dict:
    """Galaksi haritasını ve başlangıç durumunu yapılandırır."""
    if baslangic not in gezegenler:
        raise ValueError(f"Başlangıç gezegeni '{baslangic}' gezegenler listesinde yok!")
        
    yakit = kwargs.get("yakit", 50)
    return {
        "konum": baslangic,
        "yakit": yakit,
        "gezegenler": gezegenler,
        "baglantilar": baglantilar
    }

def galaksiyi_yukle(dosya_yolu: str = "uzay_oyunu/galaksi.json") -> dict:
    with open(dosya_yolu, "r", encoding="utf-8") as f:
        veri = json.load(f)
    return galaksi_kur(**veri)