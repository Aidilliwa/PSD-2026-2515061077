# Simulasi Riwayat File yang Dibuka Menggunakan Stack Array

Program ini dibuat untuk mensimulasikan riwayat file yang telah dibuka pada sebuah aplikasi komputer. Setiap file yang dibuka akan disimpan ke dalam stack, sehingga file terakhir yang dibuka akan berada di posisi paling atas dan ditampilkan terlebih dahulu.

Struktur data yang digunakan pada program ini adalah Stack berbasis Array dengan konsep LIFO (Last In First Out). Yaitu data terakhir yang masuk akan menjadi data pertama yang keluar. metode ini cocok digunakan untuk mencatat riwayat file karena file yang terakhir dibuka merupakan file yang paling atas pada daftar riwayat.

---

## Source Code

<img width="669" height="785" alt="Source Code 1" src="https://github.com/user-attachments/assets/0b945146-3b29-47ed-a87f-b4fc972c8d99" />

<img width="606" height="794" alt="Source Code 2" src="https://github.com/user-attachments/assets/a9880f7f-8587-4216-8b39-4b1f41a87f56" />


Baris 1: Mendefinisikan class StackArray

Baris 2: Konstruktor class untuk inisialisasi stack

Baris 3: Menentukan kapasitas maksimum stack

Baris 4: Membuat array kosong sebagai tempat penyimpanan data

Baris 5: Menginisialisasi indeks top dengan nilai -1

Baris 7: Mendefinisikan fungsi is_empty

Baris 8: Mengecek apakah stack kosong

Baris 10: Mendefinisikan fungsi is_full

Baris 11: Mengecek apakah stack penuh

Baris 13: Mendefinisikan fungsi push untuk menambah data

Baris 14: Mengecek apakah stack penuh

Baris 15: Menampilkan pesan jika stack penuh

Baris 16: Menghentikan proses

Baris 17: Menambah indeks top

Baris 18: Menyimpan data file ke stack

Baris 19: Menampilkan pesan file berhasil dibuka

Baris 21: Mendefinisikan fungsi pop untuk menghapus data teratas

Baris 22: Mengecek apakah stack kosong

Baris 23: Menampilkan pesan jika stack kosong

Baris 24: Menghentikan proses

Baris 25: Menampilkan file terakhir yang ditutup

Baris 26: Mengurangi indeks top

Baris 28: Mendefinisikan fungsi peek

Baris 29: Mengecek apakah stack kosong

Baris 30: Menampilkan pesan jika stack kosong

Baris 31: Menghentikan proses

Baris 32: Menampilkan file terakhir dibuka

Baris 34: Mendefinisikan fungsi display

Baris 35: Mengecek apakah stack kosong

Baris 36: Menampilkan pesan jika stack kosong

Baris 37: Menghentikan proses

Baris 38: Menampilkan judul riwayat file

Baris 39: Perulangan untuk menampilkan isi stack dari atas ke bawah

Baris 40: Menampilkan data file

Baris 41: Pindah ke baris baru

Baris 44: Mendefinisikan fungsi utama main()

Baris 45: Membuat objek stack

Baris 46: Inisialisasi variabel pilihan menu

Baris 48–53: Menampilkan menu program

Baris 55–59: Input pilihan menu dengan validasi error

Baris 61–66: Proses membuka file dan memasukkan ke stack

Baris 68–69: Menjalankan fungsi pop untuk menutup file

Baris 71–72: Menjalankan fungsi peek untuk melihat file terakhir

Baris 74–75: Menampilkan seluruh riwayat file

Baris 77–78: Menampilkan pesan program selesai

Baris 80: Menampilkan pesan jika pilihan menu tidak valid

Baris 83: Mengecek apakah file dijalankan langsung

Baris 84: Memanggil fungsi main()

## Output Program

<img width="386" height="985" alt="Output" src="https://github.com/user-attachments/assets/962b99c5-5eea-4bb7-a3fd-91069f1e7781" />

Program akan menyimpan setiap file yang dibuka ke dalam stack menggunakan operasi push. File SKPL.pdf, Komik.pdf, dan Modul.pdf dimasukkan secara berurutan sehingga file terakhir yang dibuka berada di posisi paling atas. Saat pengguna memilih menu tutup file, program menjalankan operasi pop sehingga file Modul.pdf berhasil ditutup terlebih dahulu sesuai konsep LIFO (Last In First Out). Setelah itu, ketika pengguna memilih menu lihat file terakhir, program menampilkan Komik.pdf sebagai file yang berada di posisi teratas. Pada menu tampilkan riwayat file, program menampilkan urutan file dari terbaru ke terlama yaitu Komik.pdf | SKPL.pdf.

## Link YouTube


