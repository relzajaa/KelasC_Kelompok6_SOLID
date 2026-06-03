from interfaces import Hewan, HewanBerjalan, HewanTerbang, HewanBerenang
from suara import SuaraKucing, SuaraIkan, SuaraBurung, SuaraPenguin, SuaraBebek


# Kucing hanya berjalan
class Kucing(Hewan, HewanBerjalan):
    def __init__(self, nama):
        super().__init__(nama, "Mamalia")
        self._suara = SuaraKucing()

    def suara(self):
        self._suara.bersuara(self.nama)

    def berjalan(self):
        print(f"{self.nama} sedang berjalan santai.")


# Ikan hanya berenang
class Ikan(Hewan, HewanBerenang):
    def __init__(self, nama):
        super().__init__(nama, "Ikan")
        self._suara = SuaraIkan()

    def suara(self):
        self._suara.bersuara(self.nama)

    def berenang(self):
        print(f"{self.nama} sedang berenang cepat.")


# Burung dapat terbang dan berjalan
class Burung(Hewan, HewanTerbang, HewanBerjalan):
    def __init__(self, nama):
        super().__init__(nama, "Burung")
        self._suara = SuaraBurung()

    def suara(self):
        self._suara.bersuara(self.nama)

    def terbang(self):
        print(f"{self.nama} sedang terbang tinggi.")

    def berjalan(self):
        print(f"{self.nama} sedang berjalan biasa.")


# Penguin berjalan dan berenang
class Penguin(Hewan, HewanBerjalan, HewanBerenang):
    def __init__(self, nama):
        super().__init__(nama, "Burung")
        self._suara = SuaraPenguin()

    def suara(self):
        self._suara.bersuara(self.nama)

    def berjalan(self):
        print(f"{self.nama} sedang berjalan lucu.")

    def berenang(self):
        print(f"{self.nama} sedang berenang di air dingin.")


# Bebek bisa berjalan, berenang, dan terbang
class Bebek(Hewan, HewanBerjalan, HewanBerenang, HewanTerbang):
    def __init__(self, nama):
        super().__init__(nama, "Unggas")
        self._suara = SuaraBebek()

    def suara(self):
        self._suara.bersuara(self.nama)

    def berjalan(self):
        print(f"{self.nama} sedang berjalan lambat.")

    def berenang(self):
        print(f"{self.nama} sedang berenang di sungai.")

    def terbang(self):
        print(f"{self.nama} sedang terbang rendah.")
        