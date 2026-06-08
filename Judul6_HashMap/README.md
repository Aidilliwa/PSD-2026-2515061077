# Sistem Parkir Kendaraan Menggunakan Hash Map Separate Chaining

Program ini digunakan untuk mengelola data kendaraan yang masuk ke area parkir menggunakan struktur data Hash Map. Setiap kendaraan memiliki nomor tiket sebagai key dan plat nomor sebagai value. Program dapat menambahkan, mencari, dan menghapus data kendaraan berdasarkan nomor tiket.

Struktur data yang diterapkan adalah Hash Map dengan metode Separate Chaining, yang memungkinkan penyimpanan dan pencarian data dilakukan secara cepat. Jika terjadi collision, data disimpan menggunakan linked list pada bucket yang sama sehingga tetap dapat diakses dengan baik.

---

## Source Code

<img width="728" height="712" alt="Source Code 1" src="https://github.com/user-attachments/assets/bbcf6319-c55c-4759-84c9-6ae1f2f55174" />

<img width="824" height="568" alt="Source Code 2" src="https://github.com/user-attachments/assets/73a2706c-1d47-42ef-ac8c-2e9061f07485" />

<img width="704" height="557" alt="Source Code 3" src="https://github.com/user-attachments/assets/879cf28c-d27c-43aa-b840-bdd787d3eeb2" />

Baris 1: Membuat class Node.

Baris 2: Membuat konstruktor class Node.

Baris 3: Menyimpan nomor tiket sebagai key.

Baris 4: Menyimpan plat nomor kendaraan sebagai value.

Baris 5: Menginisialisasi pointer next dengan None.

Baris 8: Membuat class HashMapSeparateChaining.

Baris 9: Membuat konstruktor class HashMapSeparateChaining.

Baris 10: Menyimpan ukuran hash table ke variabel SIZE.

Baris 11: Membuat hash table berisi nilai None.

Baris 13: Membuat fungsi hash_function().

Baris 14: Menghitung indeks hash berdasarkan key.

Baris 16: Membuat fungsi insert().

Baris 17: Menentukan indeks hash dari key yang dimasukkan.

Baris 18: Mengambil node pertama pada bucket yang sesuai.

Baris 20: Memeriksa apakah masih ada node pada linked list.

Baris 21: Mengecek apakah key sudah ada.

Baris 22: Memperbarui value jika key ditemukan.

Baris 23: Mengakhiri proses insert jika key sudah ada.

Baris 24: Berpindah ke node berikutnya.

Baris 26: Membuat node baru.

Baris 27: Menghubungkan node baru ke awal linked list.

Baris 28: Menyimpan node baru ke bucket hash table.

Baris 30: Membuat fungsi search().

Baris 31: Menentukan indeks hash dari key yang dicari.

Baris 32: Mengambil node pertama pada bucket.

Baris 34: Menelusuri linked list pada bucket.

Baris 35: Memeriksa apakah key ditemukan.

Baris 36: Mengembalikan node yang ditemukan.

Baris 37: Berpindah ke node berikutnya.

Baris 39: Mengembalikan None jika key tidak ditemukan.

Baris 41: Membuat fungsi remove_key().

Baris 42: Menentukan indeks hash dari key yang akan dihapus.

Baris 43: Mengambil node pertama pada bucket.

Baris 44: Membuat variabel prev untuk menyimpan node sebelumnya.

Baris 46: Menelusuri linked list pada bucket.

Baris 47: Mengecek apakah key yang dicari ditemukan.

Baris 48: Memeriksa apakah node yang dihapus berada di awal linked list.

Baris 49: Menghapus node pertama dengan menggeser pointer bucket.

Baris 50: Jika node bukan yang pertama.

Baris 51: Menghubungkan node sebelumnya dengan node setelahnya.

Baris 53: Mengembalikan nilai True jika penghapusan berhasil.

Baris 55: Memindahkan prev ke node saat ini.

Baris 56: Berpindah ke node berikutnya.

Baris 58: Mengembalikan False jika key tidak ditemukan.

Baris 60: Membuat fungsi display().

Baris 61: Menampilkan judul isi hash table.

Baris 62: Melakukan perulangan untuk setiap bucket.

Baris 63: Menampilkan nomor indeks bucket.

Baris 64: Mengambil node pertama pada bucket.

Baris 66: Menelusuri linked list dalam bucket.

Baris 67: Menampilkan data tiket dan plat kendaraan.

Baris 68: Berpindah ke node berikutnya.

Baris 70: Menampilkan NULL sebagai penanda akhir linked list.

Baris 73: Membuat fungsi main().

Baris 74: Membuat objek HashMapSeparateChaining.

Baris 76: Memberikan komentar bahwa data berikut adalah kendaraan yang masuk area parkir.

Baris 77: Menambahkan data tiket 101 dengan plat nomor BE2515XLD.

Baris 78: Menambahkan data tiket 111 dengan plat nomor BE1077VRS.

Baris 79: Menambahkan data tiket 121 dengan plat nomor BE6090KGH.

Baris 80: Menambahkan data tiket 102 dengan plat nomor BE3553FNE.

Baris 82: Menampilkan seluruh data kendaraan dalam hash table.

Baris 84: Memberikan komentar bahwa proses berikut adalah pencarian data kendaraan.

Baris 85: Mencari data kendaraan dengan tiket 111.

Baris 87: Memeriksa apakah data ditemukan.

Baris 88: Menampilkan plat nomor kendaraan jika ditemukan.

Baris 89: Menjalankan kondisi selain jika data tidak ditemukan.

Baris 90: Menampilkan pesan bahwa tiket tidak ditemukan.

Baris 92: Memberikan komentar bahwa proses berikut adalah penghapusan data kendaraan.

Baris 93: Menghapus data kendaraan dengan tiket 111.

Baris 95: Menampilkan informasi setelah kendaraan keluar dari area parkir.

Baris 96: Menampilkan kembali isi hash table setelah penghapusan data.

Baris 99: Memeriksa apakah program dijalankan secara langsung.

Baris 100: Memanggil fungsi main() untuk menjalankan program.

## Output Program

<img width="697" height="411" alt="Output" src="https://github.com/user-attachments/assets/d79953db-ed73-4b44-b19f-745af19c1e0c" />

Output program menampilkan data kendaraan yang tersimpan di dalam Hash Table berdasarkan nomor tiket parkir sebagai key dan plat nomor kendaraan sebagai value. Pada tampilan awal, terdapat empat data kendaraan yang berhasil dimasukkan ke dalam Hash Map. Karena menggunakan metode Separate Chaining, beberapa data dengan indeks hash yang sama disimpan dalam bentuk linked list pada bucket yang sama. 

Selanjutnya program melakukan pencarian terhadap tiket parkir 111 dan berhasil menemukan kendaraan dengan plat nomor BE1077VRS. Setelah itu, data kendaraan dengan tiket 111 dihapus untuk mensimulasikan kendaraan yang keluar dari area parkir. Ketika Hash Table ditampilkan kembali, data tiket 111 sudah tidak ada, sedangkan data kendaraan lainnya tetap tersimpan. Hal ini menunjukkan bahwa proses insert, search, dan delete pada Hash Map berhasil berjalan dengan baik tanpa error.

## Link YouTube


