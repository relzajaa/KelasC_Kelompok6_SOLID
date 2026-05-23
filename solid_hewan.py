from abc import ABC, abstractmethod

# Abstraksi dasar hewan
class Hewan(ABC):
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def makan(self):
        print(f"{self.nama} sedang makan.")

    def tidur(self):
        print(f"{self.nama} sedang tidur.")

    @abstractmethod
    def suara(self):
        pass

# Interface khusus hewan berjalan
class HewanBerjalan(ABC):
    @abstractmethod
    def berjalan(self):
        pass

# Interface khusus hewan terbang
class HewanTerbang(ABC):
    @abstractmethod
    def terbang(self):
        pass

# Interface khusus hewan berenang
class HewanBerenang(ABC):
    @abstractmethod
    def berenang(self):
        pass

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
        print(f"{self.nama} bersuara Blup Blup.")

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

# =========================================================
# Baru sampai sini tadi
# =========================================================

class Kandang:
    def __init__(self):
        self.hewan_list = []

    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)

    def bersihkan_kandang(self):
        print("Kandang dibersihkan.")

class KebunBinatang:
    def __init__(self):
        self.kandang = Kandang()

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            hewan.terbang()
