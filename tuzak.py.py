# uzay_oyunu/tuzak.py

def yakit_ekle(miktar: int, depo: list = None) -> list:
    """Mutable default argument tuzağını önleyen güvenli fonksiyon."""
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo