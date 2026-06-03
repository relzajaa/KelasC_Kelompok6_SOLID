# Product Requirements Document (PRD)

## 1. Pendahuluan

### 1.1 Tujuan
Dokumen ini menguraikan spesifikasi kebutuhan (requirements) untuk sistem **"Simulasi Kebun Binatang"**. Program ini adalah aplikasi Python sederhana yang mensimulasikan kebun binatang dengan fokus utama pada penerapan **Prinsip SOLID** dalam Pemrograman Berorientasi Objek (OOP).

### 1.2 Ruang Lingkup
Sistem akan memodelkan berbagai entitas hewan dengan perilaku spesifiknya (seperti berjalan, terbang, atau berenang), pengelolaan penyimpanan hewan dalam kandang, perawatan hewan, serta rutinitas pembersihan. Arsitektur kode dirancang agar modular dengan memisahkannya ke beberapa modul terpisah (`interfaces.py`, `suara.py`, `hewan.py`, `kandang.py`, `kebun_binatang.py`, dan `main.py`).

---

## 2. Deskripsi Sistem
Program "Simulasi Kebun Binatang" adalah aplikasi berbasis modular Python yang mampu:
- Mendefinisikan dan membuat instansiasi berbagai jenis hewan berdasarkan taksonomi dan kemampuannya (Mamalia, Burung, Ikan, Unggas).
- Mengelola koleksi objek hewan di dalam suatu fasilitas Kandang.
- Menampilkan daftar koleksi hewan yang ada di kebun binatang ke layar.
- Melakukan simulasi pembersihan kandang.
- Merawat seluruh hewan dengan memastikan setiap entitas melakukan perilakunya (makan, berjalan, berenang, terbang) sesuai dengan kapasitas dan antarmuka (interface) yang dimilikinya secara aman.
- Memisahkan logika pensuaraan hewan ke dalam komponen tersendiri untuk mendukung fleksibilitas pemeliharaan kode.

---

## 3. Fitur dan Persyaratan Utama (Requirements)

### 3.1 Manajemen Hewan
- **Pembuatan Objek:** Sistem harus dapat membuat objek hewan spesifik, misalnya: Kucing, Ikan, Burung, Penguin, dan Bebek.
- **Atribut Dasar:** Setiap hewan harus memiliki properti `nama` dan `jenis`.
- **Perilaku Dasar:** Setiap hewan harus memiliki kemampuan dasar yaitu `makan()` dan `tidur()`.
- **Perilaku Khusus (Interface Segregation):** Kemampuan khusus seperti berjalan, berenang, dan terbang harus diimplementasikan secara terpisah melalui Interface/Class Abstrak yang spesifik (misal: `HewanBerjalan`, `HewanBerenang`, `HewanTerbang` di `interfaces.py`).
- **Pendelegasian Suara (Strategy Pattern):** Logika bersuara tidak di-hardcode dalam kelas hewan, melainkan didelegasikan ke objek strategi suara yang terpisah di `suara.py`.

### 3.2 Manajemen Kandang
- **Penyimpanan:** Sistem harus dapat menambahkan hewan ke dalam Kandang menggunakan metode `tambah_hewan()`.
- **Penghapusan:** Sistem harus dapat mengeluarkan/menghapus hewan dari Kandang berdasarkan namanya menggunakan metode `hapus_hewan()`.
- **Enkapsulasi (Single Responsibility):** Class `Kandang` murni bertugas mengelola koleksi data hewan, memisahkan logika penyimpanan dari logika presentasi/tampilan.

### 3.3 Penampil Informasi Kandang
- **Fungsi Menampilkan:** Sistem harus memiliki modul terpisah (`PenampilKandang` di `kandang.py`) untuk menampilkan daftar seluruh hewan yang ada di dalam Kandang beserta urutannya.
- **Penanganan Kondisi Kosong:** Jika kandang kosong, sistem harus memberikan notifikasi yang sesuai.

### 3.4 Pembersihan Kandang
- **Simulasi Pembersihan:** Sistem memiliki fungsi spesifik (`PembersihKandang` di `kandang.py`) untuk mensimulasikan proses pembersihan kandang.

### 3.5 Simulasi Perawatan di Kebun Binatang
- **Tanggung Jawab Utama:** Sistem memiliki class `KebunBinatang` yang bertugas mengeksekusi simulasi perawatan (`rawat_semua_hewan()`).
- **Eksekusi Aman (Liskov Substitution):** Saat merawat, sistem memicu aktivitas spesifik hewan secara aman melalui pemeriksaan kemampuan (menggunakan `isinstance()`). Tidak ada hewan yang dipaksa melakukan metode yang bukan kemampuannya (misal: kucing tidak akan dipaksa terbang).
- **Injeksi Dependensi (Dependency Inversion):** Class `KebunBinatang` tidak membuat objek `Kandang` secara langsung. Ia menerima objek Kandang (yang diinjeksikan) sehingga memiliki ketergantungan pada abstraksi, bukan implementasi konkrit.

---

## 4. Penerapan Prinsip SOLID
PRD ini mendefinisikan persyaratan penerapan 5 Prinsip SOLID:

1. **S - Single Responsibility Principle (SRP):** Tanggung jawab dipecah ke kelas `Kandang` (penyimpanan), `PenampilKandang` (tampilan), `PembersihKandang` (utilitas kebersihan), dan pemisahan logika suara ke modul `suara.py`.
2. **O - Open/Closed Principle (OCP):** Kode terbuka untuk diperluas. Penambahan hewan baru (contoh: Buaya) atau variasi suara baru (contoh: Suara Buaya) hanya perlu menambahkan kelas baru di file yang bersangkutan tanpa harus memodifikasi source code kelas yang sudah ada.
3. **L - Liskov Substitution Principle (LSP):** Class `KebunBinatang` dapat melakukan iterasi ke seluruh subclass `Hewan` dan memanggil perilakunya secara dinamis dan aman karena sistem menjamin substitusi yang sah dari masing-masing tipe interface.
4. **I - Interface Segregation Principle (ISP):** Interface dipecah-pecah (`HewanBerjalan`, `HewanTerbang`, `HewanBerenang`) agar subclass (seperti `Ikan`) tidak bergantung pada atau diwajibkan mengimplementasikan metode yang tidak ia butuhkan (seperti `terbang()`).
5. **D - Dependency Inversion Principle (DIP):** `KebunBinatang` menerima `Kandang` melalui injeksi dependensi. Kelas hewan juga bergantung pada abstraksi `SuaraHewan` (melalui Strategy Pattern) dan bukan kelas konkret secara langsung.

---

## 5. Batasan dan Spesifikasi Teknis
- **Bahasa Pemrograman:** Python 3.x
- **Lingkungan Antarmuka:** Command Line Interface (CLI)
- **Persyaratan Library:** Hanya menggunakan modul standar bawaan Python (seperti modul `abc` untuk Abstract Base Class). Tidak memerlukan library eksternal/pihak ketiga (No Dependencies).
- **Penyimpanan Data:** Menyimpan data hewan secara *in-memory* (menggunakan list di Python), tanpa menggunakan database persisten.
