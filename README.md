# Penerapan SOLID Principle pada Program Kebun Binatang

Repositori atau direktori ini berisi contoh penerapan **SOLID Principles** dalam pemrograman berorientasi objek menggunakan bahasa Python. Kode utama terdapat pada file `solid_hewan.py`.

## Apa itu SOLID?

SOLID adalah singkatan dari lima prinsip desain berorientasi objek yang bertujuan membuat desain perangkat lunak menjadi lebih mudah dipahami, fleksibel, dan mudah dipelihara (maintainable).

1. **S** - Single Responsibility Principle (SRP)
2. **O** - Open/Closed Principle (OCP)
3. **L** - Liskov Substitution Principle (LSP)
4. **I** - Interface Segregation Principle (ISP)
5. **D** - Dependency Inversion Principle (DIP)

## Penjelasan Implementasi SOLID pada `solid_hewan.py`

### 1. Single Responsibility Principle (SRP)
Sebuah class hanya boleh memiliki satu alasan untuk berubah (satu tanggung jawab).
* **Sebelum Refactor**: Class `Kandang` menyimpan data hewan, menampilkan daftar hewan ke layar, sekaligus bertugas membersihkan kandang.
* **Setelah Refactor**:
  - `Kandang`: Hanya bertugas menyimpan data (list) hewan dan menambah/menghapus hewan.
  - `PenampilKandang`: Khusus bertugas menampilkan list hewan.
  - `PembersihKandang`: Khusus bertugas untuk simulasi pembersihan kandang.

### 2. Open/Closed Principle (OCP)
Class harus terbuka untuk ekstensi (perluasan) tetapi tertutup untuk modifikasi.
* Struktur class hierarki pewarisan hewan (seperti penambahan hewan baru `Burung`, `Kucing`, atau `Bebek`) sangat mudah dilakukan dengan meng-extend class `Hewan` dan interface terkait (seperti `HewanTerbang`) tanpa perlu mengubah kode pada class dasar `Hewan`.

### 3. Liskov Substitution Principle (LSP)
Objek dari superclass harus dapat digantikan oleh objek dari subclass-nya tanpa merusak fungsionalitas program.
* Pada class `KebunBinatang` metode `rawat_semua_hewan`, program mengecek interface atau kemampuan tiap objek terlebih dahulu menggunakan `isinstance()`:
  - Jika `HewanTerbang`, baru memanggil `terbang()`.
  - Jika `HewanBerjalan`, baru memanggil `berjalan()`.
* Hal ini mencegah error yang terjadi jika kita memaksa (contohnya) seekor Kucing untuk terbang, yang mana melanggar LSP karena Kucing tidak dapat menggantikan sifat burung secara keseluruhan.

### 4. Interface Segregation Principle (ISP)
Klien tidak boleh dipaksa untuk bergantung pada interface (metode) yang tidak mereka gunakan.
* Daripada membuat satu interface besar dengan fungsi `terbang()`, `berjalan()`, dan `berenang()` untuk semua `Hewan`, program memecahnya menjadi:
  - `HewanBerjalan`
  - `HewanTerbang`
  - `HewanBerenang`
* Seekor `Ikan` hanya mengimplementasikan `HewanBerenang`, sehingga tidak ada metode `terbang()` atau `berjalan()` tak berguna yang menempel pada `Ikan`.

### 5. Dependency Inversion Principle (DIP)
Modul tingkat tinggi (high-level) tidak boleh bergantung pada modul tingkat rendah (low-level). Keduanya harus bergantung pada abstraksi.
* **Sebelum Refactor**: Class `KebunBinatang` (high-level) langsung menginisiasi objek `Kandang` (low-level) di dalam *constructor* nya (`self.kandang = Kandang()`).
* **Setelah Refactor**: `KebunBinatang` menerima `Kandang` (atau abstraksi kandang) lewat injeksi dependensi melalui *parameter constructor*:
  ```python
  def __init__(self, kandang: Kandang):
      self.kandang = kandang
  ```

## Cara Menjalankan

Anda dapat menjalankan skrip ini menggunakan Python 3.

```bash
python solid_hewan.py
```

Anda akan melihat simulasi program mendaftarkan hewan, menampilkan isi kandang, merawat hewan (hewan akan melakukan perilakunya masing-masing seperti makan, berjalan, terbang, dll sesuai dengan kemampuannya), hingga mengeluarkan hewan dari kandang.