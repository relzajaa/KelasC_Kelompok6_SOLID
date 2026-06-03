from hewan import Kucing, Ikan, Burung, Penguin, Bebek
from interfaces import Hewan


class Kandang:
    def __init__(self):
        self.hewan_list = []

    # Menambahkan hewan ke kandang
    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)
        print(f"{hewan.nama} berhasil dimasukkan ke kandang.")

    # Menghapus hewan dari kandang
    def hapus_hewan(self, nama_hewan):
        for hewan in self.hewan_list:
            if hewan.nama == nama_hewan:
                self.hewan_list.remove(hewan)
                print(f"{nama_hewan} berhasil dikeluarkan dari kandang.")
                return
        print(f"Hewan dengan nama {nama_hewan} tidak ditemukan.")


# SRP: Memisahkan tanggung jawab menampilkan informasi hewan dari class Kandang
class PenampilKandang:
    @staticmethod
    def tampilkan_hewan(kandang):
        print("\nDaftar Hewan di Kandang:")

        if not kandang.hewan_list:
            print("Kandang masih kosong.")
            return

        for index, hewan in enumerate(kandang.hewan_list, start=1):
            print(f"{index}. {hewan.nama} - {hewan.jenis}")


# SRP: Memisahkan tanggung jawab membersihkan kandang dari class Kandang
class PembersihKandang:
    @staticmethod
    def bersihkan_kandang():
        print("\nKandang sedang dibersihkan...")
        print("Kandang berhasil dibersihkan.")
