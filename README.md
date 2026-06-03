# Penerapan SOLID Principle pada Program Kebun Binatang

Repositori ini berisi contoh penerapan **SOLID Principles** dalam pemrograman berorientasi objek menggunakan bahasa Python. Kode asli yang bersifat satu file telah didekonstruksi ke dalam modul-modul terpisah untuk mematuhi prinsip desain yang bersih dan modular.

## Struktur Proyek

Setelah refaktorisasi, kode dipecah menjadi beberapa file berikut:

* **[interfaces.py](file:///d:/Materi%20Kuliah/Semester%202/Pemrograman%20Berorientasi%20Objek/KelasC_Kelompok6_SOLID/interfaces.py)**: Berisi kelas dasar abstrak (Abstract Base Classes) untuk hewan serta antarmuka khusus (`HewanBerjalan`, `HewanTerbang`, `HewanBerenang`).
* **[suara.py](file:///d:/Materi%20Kuliah/Semester%202/Pemrograman%20Berorientasi%20Objek/KelasC_Kelompok6_SOLID/suara.py)**: Berisi kelas strategi suara hewan (`SuaraHewan` beserta turunannya) menggunakan **Strategy Pattern**.
* **[hewan.py](file:///d:/Materi%20Kuliah/Semester%202/Pemrograman%20Berorientasi%20Objek/KelasC_Kelompok6_SOLID/hewan.py)**: Berisi implementasi konkret hewan (`Kucing`, `Ikan`, `Burung`, `Penguin`, `Bebek`) yang menggunakan interface dan strategi suara.
* **[kandang.py](file:///d:/Materi%20Kuliah/Semester%202/Pemrograman%20Berorientasi%20Objek/KelasC_Kelompok6_SOLID/kandang.py)**: Mengelola penyimpanan hewan, penampil daftar hewan, dan pembersih kandang secara terpisah.
* **[kebun_binatang.py](file:///d:/Materi%20Kuliah/Semester%202/Pemrograman%20Berorientasi%20Objek/KelasC_Kelompok6_SOLID/kebun_binatang.py)**: Berisi proses simulasi perawatan kebun binatang.
* **[main.py](file:///d:/Materi%20Kuliah/Semester%202/Pemrograman%20Berorientasi%20Objek/KelasC_Kelompok6_SOLID/main.py)**: Entry point utama untuk menjalankan seluruh simulasi program.
* **[solid_hewan.py](file:///d:/Materi%20Kuliah/Semester%202/Pemrograman%20Berorientasi%20Objek/KelasC_Kelompok6_SOLID/solid_hewan.py)** *(Lama)*: Kode asli sebelum dipecah menjadi modul-modul terpisah.

---

## Penjelasan Implementasi SOLID

### 1. Single Responsibility Principle (SRP)
Sebuah kelas hanya boleh memiliki satu alasan untuk berubah.
* **Implementasi**:
  - `Kandang`: Hanya bertugas menyimpan data (list) hewan dan menambah/menghapus hewan.
  - `PenampilKandang`: Khusus bertugas menampilkan list hewan ke layar.
  - `PembersihKandang`: Khusus bertugas mensimulasikan pembersihan kandang.
  - Modul suara dipisah ke [suara.py](file:///d:/Materi%20Kuliah/Semester%202/Pemrograman%20Berorientasi%20Objek/KelasC_Kelompok6_SOLID/suara.py), memisahkan tanggung jawab logika suara dari entitas hewan itu sendiri.

### 2. Open/Closed Principle (OCP)
Kelas harus terbuka untuk perluasan (extension) tetapi tertutup untuk modifikasi (modification).
* **Implementasi**:
  - Struktur pewarisan kelas hewan memudahkan penambahan hewan baru tanpa mengubah kelas dasar `Hewan` di [interfaces.py](file:///d:/Materi%20Kuliah/Semester%202/Pemrograman%20Berorientasi%20Objek/KelasC_Kelompok6_SOLID/interfaces.py).
  - Dengan menggunakan **Strategy Pattern** untuk suara di [suara.py](file:///d:/Materi%20Kuliah/Semester%202/Pemrograman%20Berorientasi%20Objek/KelasC_Kelompok6_SOLID/suara.py), kita dapat menambahkan suara baru dengan membuat kelas turunan baru dari `SuaraHewan` tanpa mengubah logika kelas suara yang lain.

### 3. Liskov Substitution Principle (LSP)
Objek dari superclass harus dapat digantikan oleh objek dari subclass-nya tanpa merusak fungsionalitas program.
* **Implementasi**:
  - Dalam `KebunBinatang.rawat_semua_hewan()`, program memeriksa antarmuka kemampuan tiap objek terlebih dahulu menggunakan `isinstance()` sebelum memanggil metode spesifiknya. Hal ini menghindari pemanggilan metode ilegal (seperti memaksa kucing untuk terbang).

### 4. Interface Segregation Principle (ISP)
Klien tidak boleh dipaksa untuk bergantung pada antarmuka (metode) yang tidak mereka gunakan.
* **Implementasi**:
  - Daripada menyatukan fungsi `terbang()`, `berjalan()`, dan `berenang()` di dalam satu kelas dasar `Hewan`, antarmuka tersebut dipisahkan menjadi kelas independen (`HewanBerjalan`, `HewanTerbang`, `HewanBerenang`). Setiap hewan hanya mengimplementasikan kelas antarmuka yang sesuai dengan kemampuannya.

### 5. Dependency Inversion Principle (DIP)
Modul tingkat tinggi tidak boleh bergantung pada modul tingkat rendah. Keduanya harus bergantung pada abstraksi.
* **Implementasi**:
  - `KebunBinatang` (modul tingkat tinggi) menerima objek `Kandang` (modul tingkat rendah) melalui parameter konstruktor (*dependency injection*), alih-alih melakukan instansiasi langsung di dalam konstruktornya.
  - Setiap kelas hewan menerima strategi suaranya menggunakan abstraksi dari `SuaraHewan`, bukan langsung memprogram teks suara secara *hardcoded* di dalam tubuh kelas hewan.

---

## Cara Menjalankan

Anda dapat menjalankan simulasi program menggunakan perintah berikut:

```bash
py main.py
```
atau
```bash
python main.py
```