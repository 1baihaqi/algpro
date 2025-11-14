# Proyek Algoritma dan Pemrograman: Kalkulator Web Interaktif

Ini adalah proyek aplikasi web sederhana yang berfungsi sebagai kalkulator untuk berbagai operasi algoritma. Aplikasi ini dibangun dengan backend **Flask (Python)** untuk logika komputasi dan frontend **HTML + JavaScript** vanilla untuk antarmuka pengguna.

##  Daftar Fitur

Aplikasi ini menyediakan antarmuka untuk melakukan beberapa operasi komputasi:

* **Operasi Matriks Unary:** Menghitung **determinan** dan **invers** dari matriks yang diberikan.
* **Operasi Matriks Biner:** Melakukan **penjumlahan**, **pengurangan**, dan **perkalian** antara dua matriks.
* **Pencarian Sequential:** Mendemonstrasikan algoritma pencarian sequential pada daftar angka dan menunjukkan langkah-langkah pencariannya.

## Hal-hal yang kami gunakan

* **Backend:**
    * **Python 3**
    * **Flask:** Untuk membuat REST API dan melayani file frontend.
    * **NumPy:** Untuk semua komputasi matriks yang berat.
    * **Flask-CORS:** Untuk mengizinkan permintaan (request) dari frontend.
* **Frontend:**
    * **HTML5**
    * **Tailwind CSS:** Untuk styling UI.
    * **JavaScript (Vanilla):** Untuk menangani interaksi UI dan melakukan panggilan `fetch` ke API backend.

##  Struktur File Proyek

Berikut adalah struktur file yang direkomendasikan agar proyek ini berjalan dengan benar (berdasarkan kode di `app.py`).
Anda benar, struktur yang Anda tempelkan tadi susunannya (indentasinya) sedikit keliru.

Berdasarkan app.py yang mengharapkan index.html berada di dalam folder static, struktur file yang benar untuk bagian README.md Anda seharusnya terlihat seperti ini:
├── app.py                  # Server Flask (API utama)
├── calculator.py           # Modul logika untuk semua kalkulasi (NumPy)
├── crocodile_dataset (1).csv # Dataset (dimuat oleh app.py)
│
├── static/                 # Folder untuk file frontend
│   └── index.html          # File frontend (HTML, CSS, JS)
│   └──backend.py           # (Opsional) Script Python untuk menguji endpoint
│   └── calcs.jpeg          
│   └── proyek-buaya.jpg    
│              
└── README.md               # Dokumentasi ini



