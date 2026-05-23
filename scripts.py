import math
 
class ShapeCalculator:
    def calculate(self):
        print("Pilih bangun datar: 1. Persegi  2. Persegi Panjang  3. Lingkaran")
        choice = int(input("Masukkan pilihan: "))
 
        if choice == 1:
            sisi = float(input("Masukkan sisi persegi: "))
            luas = sisi * sisi
            keliling = 4 * sisi
        elif choice == 2:
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
        elif choice == 3:
            r = float(input("Masukkan jari-jari lingkaran: "))
            luas = math.pi * r * r
            keliling = 2 * math.pi * r
        else:
            print("Pilihan tidak valid.")
            return
 
        print(f"Luas: {luas}")
        print(f"Keliling: {keliling}")
 
if __name__ == "__main__":
    calculator = ShapeCalculator()
    calculator.calculate()