from abc import ABC, abstractmethod


# SRP (Single Responsibility Principle)
# Memisahkan tanggung jawab suara hewan ke file tersendiri.
#
# OCP (Open/Closed Principle)
# Untuk menambah suara hewan baru, cukup buat class baru
# tanpa mengubah class yang sudah ada.


class SuaraHewan(ABC):
    """Interface untuk strategi suara hewan."""

    @abstractmethod
    def bersuara(self, nama):
        pass


class SuaraKucing(SuaraHewan):
    def bersuara(self, nama):
        print(f"{nama} bersuara Miaw Miaw.")


class SuaraIkan(SuaraHewan):
    def bersuara(self, nama):
        print(f"{nama} bersuara blub blub.")


class SuaraBurung(SuaraHewan):
    def bersuara(self, nama):
        print(f"{nama} bersuara cit cit cuit.")


class SuaraPenguin(SuaraHewan):
    def bersuara(self, nama):
        print(f"{nama} bersuara hringgg.")


class SuaraBebek(SuaraHewan):
    def bersuara(self, nama):
        print(f"{nama} bersuara kwek kwek.")
