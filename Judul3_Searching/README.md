# Pencarian Nomor Kupon Undian Menggunakan Sequential Search

Program ini dibuat untuk melakukan pencarian nomor kupon undian menggunakan Sequential Search. Pengguna dapat memasukkan nomor kupon yang ingin dicari, kemudian program akan memeriksa data satu per satu hingga menemukan nomor yang sesuai.

Sequential Search bekerja dengan cara membandingkan data dari elemen pertama sampai elemen terakhir secara berurutan. Program ini juga menghitung berapa kali nomor kupon tersebut muncul dalam daftar data. Metode ini cocok digunakan untuk jumlah data yang tidak terlalu besar dan mudah dipahami dalam proses pencarian data sederhana.

---

## Source Code

<img width="626" height="719" alt="Source Code" src="https://github.com/user-attachments/assets/5263847d-0888-47b6-a18e-d50f8ce1c9fd" />


Baris 1: Mendefinisikan fungsi sequential_search dengan parameter data, jumlah data, dan target pencarian

Baris 2: Variabel i diinisialisasi dengan nilai 0 sebagai indeks awal

Baris 3: Variabel counter digunakan untuk menghitung jumlah data yang ditemukan

Baris 4: Perulangan dilakukan selama indeks masih kurang dari jumlah data

Baris 5: Mengecek apakah data pada indeks saat ini sama dengan target

Baris 6: Jika sama, nilai counter ditambah 1

Baris 7: Indeks i ditambah 1 untuk melanjutkan pencarian

Baris 8: Mengembalikan jumlah data yang ditemukan

Baris 11: Mendefinisikan fungsi utama main()

Baris 12: Komentar penjelasan data kupon undian

Baris 13: Membuat list data nomor kupon undian

Baris 15: Menyimpan jumlah data ke variabel n

Baris 17: Menampilkan teks daftar nomor kupon

Baris 18: Menampilkan isi data kupon

Baris 21: Memulai perulangan input

Baris 22: Memulai blok try

Baris 23: Input nomor kupon yang ingin dicari

Baris 24: Menghentikan perulangan jika input valid

Baris 25: Menangani error jika input bukan angka

Baris 26: Menampilkan pesan kesalahan input

Baris 29: Memanggil fungsi sequential search

Baris 32: Mengecek apakah data ditemukan

Baris 33: Menampilkan jumlah kemunculan nomor kupon jika ditemukan

Baris 35: Menampilkan pesan jika nomor kupon tidak ditemukan

Baris 38: Mengecek apakah file dijalankan langsung

Baris 39: Memanggil fungsi main()

## Output Program

<img width="286" height="62" alt="Output" src="https://github.com/user-attachments/assets/4dba8980-af91-46cf-867d-199c7323d61f" />

Program akan mencari nomor kupon 115 pada daftar data secara berurutan dari awal hingga akhir menggunakan algoritma Sequential Search. 

Karena nomor 115 muncul sebanyak 3 kali di dalam list data, maka program menampilkan hasil bahwa nomor kupon tersebut ditemukan sebanyak 3 kali.

## Link YouTube


