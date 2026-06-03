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
