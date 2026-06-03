from interfaces import Hewan, HewanBerjalan, HewanTerbang, HewanBerenang


# Kucing hanya berjalan
class Kucing(Hewan, HewanBerjalan):
    def __init__(self, nama):
        super().__init__(nama, "Mamalia")

    def suara(self):
        print(f"{self.nama} bersuara Miaw Miaw.")

    def berjalan(self):
        print(f"{self.nama} sedang berjalan santai.")


# Ikan hanya berenang
class Ikan(Hewan, HewanBerenang):
    def __init__(self, nama):
        super().__init__(nama, "Ikan")

    def suara(self):
        print(f"{self.nama} bersuara blub blub.")

    def berenang(self):
        print(f"{self.nama} sedang berenang cepat.")


# Burung dapat terbang dan berjalan
class Burung(Hewan, HewanTerbang, HewanBerjalan):
    def __init__(self, nama):
        super().__init__(nama, "Burung")

    def suara(self):
        print(f"{self.nama} bersuara cit cit cuit.")

    def terbang(self):
        print(f"{self.nama} sedang terbang tinggi.")

    def berjalan(self):
        print(f"{self.nama} sedang berjalan biasa.")


# Penguin berjalan dan berenang
class Penguin(Hewan, HewanBerjalan, HewanBerenang):
    def __init__(self, nama):
        super().__init__(nama, "Burung")

    def suara(self):
        print(f"{self.nama} bersuara hringgg.")

    def berjalan(self):
        print(f"{self.nama} sedang berjalan lucu.")

    def berenang(self):
        print(f"{self.nama} sedang berenang di air dingin.")


# Bebek bisa berjalan, berenang, dan terbang
class Bebek(Hewan, HewanBerjalan, HewanBerenang, HewanTerbang):
    def __init__(self, nama):
        super().__init__(nama, "Unggas")

    def suara(self):
        print(f"{self.nama} bersuara kwek kwek.")

    def berjalan(self):
        print(f"{self.nama} sedang berjalan lambat.")

    def berenang(self):
        print(f"{self.nama} sedang berenang di sungai.")

    def terbang(self):
        print(f"{self.nama} sedang terbang rendah.")
