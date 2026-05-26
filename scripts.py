from abc import ABC, abstractmethod


# =============================================================================
# PRINSIP SOLID PADA SISTEM KEBUN BINATANG
# =============================================================================


# ---- ISP (Interface Segregation Principle) ----------------------------------
# Interface dipisah sesuai kemampuan, sehingga class hanya perlu
# mengimplementasikan method yang benar-benar relevan.
# -----------------------------------------------------------------------------

class Hewan(ABC):
    """Abstraksi dasar untuk semua hewan (semua hewan bisa makan)."""

    def __init__(self, nama: str):
        self.nama = nama

    @abstractmethod
    def makan(self):
        pass


class BisaTerbang(ABC):
    """Interface terpisah untuk hewan yang bisa terbang."""

    @abstractmethod
    def terbang(self):
        pass


class BisaBerenang(ABC):
    """Interface terpisah untuk hewan yang bisa berenang."""

    @abstractmethod
    def berenang(self):
        pass


# ---- OCP (Open/Closed Principle) -------------------------------------------
# Menambah jenis hewan baru cukup membuat class baru (open for extension),
# tanpa mengubah class yang sudah ada (closed for modification).
# ---- LSP (Liskov Substitution Principle) ------------------------------------
# Setiap subclass bisa menggantikan parent-nya tanpa merusak program.
# Burung mengimplementasi BisaTerbang, Kucing tidak — sehingga tidak ada
# hewan yang dipaksa punya kemampuan yang tidak dimilikinya.
# -----------------------------------------------------------------------------

class Burung(Hewan, BisaTerbang):
    def makan(self):
        print(f"{self.nama} sedang makan biji-bijian.")

    def terbang(self):
        print(f"{self.nama} sedang terbang di langit.")


class Kucing(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan ikan.")


class Ikan(Hewan, BisaBerenang):
    def makan(self):
        print(f"{self.nama} sedang makan plankton.")

    def berenang(self):
        print(f"{self.nama} sedang berenang di air.")


# ---- SRP (Single Responsibility Principle) ----------------------------------
# Kandang hanya bertanggung jawab mengelola daftar hewan.
# Pembersihan dipindahkan ke class tersendiri (PembersihanKandang).
# -----------------------------------------------------------------------------

class Kandang:
    """Mengelola koleksi hewan di dalam kandang."""

    def __init__(self):
        self._hewan_list: list[Hewan] = []

    def tambah_hewan(self, hewan: Hewan):
        self._hewan_list.append(hewan)

    def get_semua_hewan(self) -> list[Hewan]:
        return list(self._hewan_list)


class PembersihanKandang:
    """Tanggung jawab tunggal: membersihkan kandang."""

    def bersihkan(self):
        print("Kandang sedang dibersihkan.")


# ---- DIP (Dependency Inversion Principle) -----------------------------------
# KebunBinatang tidak membuat Kandang sendiri di dalamnya.
# Sebaliknya, Kandang di-*inject* dari luar (dependency injection),
# sehingga KebunBinatang bergantung pada abstraksi, bukan objek konkret.
# -----------------------------------------------------------------------------

class KebunBinatang:
    """Mengelola operasional kebun binatang."""

    def __init__(self, kandang: Kandang, pembersihan: PembersihanKandang):
        self.kandang = kandang
        self.pembersihan = pembersihan

    def rawat_semua_hewan(self):
        for hewan in self.kandang.get_semua_hewan():
            hewan.makan()

            # Kemampuan khusus dipanggil hanya jika hewan memilikinya (ISP + LSP)
            if isinstance(hewan, BisaTerbang):
                hewan.terbang()
            if isinstance(hewan, BisaBerenang):
                hewan.berenang()

    def bersihkan_kandang(self):
        self.pembersihan.bersihkan()


# =============================================================================
# DEMO
# =============================================================================

if __name__ == "__main__":
    # Buat dependensi
    kandang = Kandang()
    pembersihan = PembersihanKandang()

    # Tambah berbagai jenis hewan (OCP — mudah ditambah tanpa ubah kode lama)
    kandang.tambah_hewan(Burung("Elang"))
    kandang.tambah_hewan(Kucing("Milo"))
    kandang.tambah_hewan(Ikan("Nemo"))

    # Inject dependensi ke KebunBinatang (DIP)
    kebun = KebunBinatang(kandang, pembersihan)

    print("=== Merawat Semua Hewan ===")
    kebun.rawat_semua_hewan()

    print()
    print("=== Membersihkan Kandang ===")
    kebun.bersihkan_kandang()