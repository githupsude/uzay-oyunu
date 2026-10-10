def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Oyuncunun sahip olduğu eşyaları metin olarak döndürür."""
    esyalar = []

    if credits:
        esyalar.append("bol kredin")

    if engines:
        esyalar.append("yetenekli bir pilot")

    if copilot:
        esyalar.append("bir yardımcı pilot")

    if not esyalar:
        return ""

    return "Sende: " + ", ".join(esyalar)


def hedef_menusu(hedefler: list[str]) -> str:
    """Hedefleri numaralandırarak menü metni olarak döndürür."""
    satirlar = []

    for i, hedef in enumerate(hedefler, start=1):
        satirlar.append(f"[{i}] {hedef}")

    return "\n".join(satirlar)