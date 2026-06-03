from hewan import Kucing, Ikan, Burung, Penguin, Bebek
from kandang import Kandang, PenampilKandang, PembersihKandang
from kebun_binatang import KebunBinatang


if __name__ == "__main__":
    # Membuat kandang
    kandang = Kandang()

    # Membuat hewan
    kucing = Kucing("Tom")
    ikan = Ikan("Piko")
    burung = Burung("Pipit")
    penguin = Penguin("Pinky")
    bebek = Bebek("Dora")

    # Memasukkan hewan ke kandang
    kandang.tambah_hewan(kucing)
    kandang.tambah_hewan(ikan)
    kandang.tambah_hewan(burung)
    kandang.tambah_hewan(penguin)
    kandang.tambah_hewan(bebek)

    # Menampilkan hewan di kandang
    penampil = PenampilKandang()
    penampil.tampilkan_hewan(kandang)

    # Membersihkan kandang
    pembersih = PembersihKandang()
    pembersih.bersihkan_kandang()

    # Membuat kebun binatang
    kebun_binatang = KebunBinatang(kandang)

    # Merawat semua hewan
    kebun_binatang.rawat_semua_hewan()

    # Menghapus hewan dari kandang
    kandang.hapus_hewan("Tom")
    penampil.tampilkan_hewan(kandang)
