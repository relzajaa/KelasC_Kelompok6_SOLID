from interfaces import HewanTerbang, HewanBerjalan, HewanBerenang
from kandang import Kandang


class KebunBinatang:
    def __init__(self, kandang: Kandang):
        self.kandang = kandang

    def rawat_semua_hewan(self):
        for hewan in self.kandang.hewan_list:
            hewan.makan()
            
            if isinstance(hewan, HewanTerbang):
                hewan.terbang()
            if isinstance(hewan, HewanBerjalan):
                hewan.berjalan()
            if isinstance(hewan, HewanBerenang):
                hewan.berenang()
