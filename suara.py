from abc import ABC, abstractmethod


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
