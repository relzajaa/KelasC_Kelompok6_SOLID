from interfaces import HewanTerbang, HewanBerjalan, HewanBerenang
from kandang import Kandang


class KebunBinatang:
    # DIP (Dependency Inversion Principle)
    # KebunBinatang menerima objek Kandang (injeksi dependensi)
    # bukannya membuat instance Kandang secara langsung di dalam constructor.
    def __init__(self, kandang: Kandang):
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()

            # LSP (Liskov Substitution Principle)
            # Mengecek kemampuan hewan sebelum memanggil fungsinya.
            # Hal ini mencegah error saat memanggil hewan.terbang() pada hewan yang tidak bisa terbang.
            if isinstance(hewan, HewanTerbang):
                hewan.terbang()
            if isinstance(hewan, HewanBerjalan):
                hewan.berjalan()
            if isinstance(hewan, HewanBerenang):
                hewan.berenang()
