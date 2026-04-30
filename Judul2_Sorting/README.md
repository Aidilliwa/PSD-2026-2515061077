# Pengurutan Harga Barang Menggunakan Algoritma Insertion Sort

Program ini dibuat untuk mengurutkan data harga barang yang dimasukkan oleh pengguna. Pengguna diminta memasukkan jumlah barang, kemudian memasukkan harga dari masing-masing barang. Data tersebut kemudian akan ditampilkan sebelum dan sesudah proses pengurutan.

Algoritma yang digunakan dalam program ini adalah Insertion Sort, yaitu metode pengurutan sederhana dengan cara menyisipkan elemen ke posisi yang tepat dalam bagian array yang sudah terurut. Algoritma ini bekerja dengan membandingkan setiap elemen dengan elemen sebelumnya, lalu memindahkannya hingga berada pada posisi yang sesuai.

---

## Source Code

<img width="570" height="660" alt="Source Code" src="https://github.com/user-attachments/assets/698ea1c1-d95b-498b-b596-fa7635d5380a" />

Baris 1: Mendefinisikan fungsi insertion_sort dengan parameter array dan jumlah data

Baris 2: Perulangan dimulai dari indeks ke-1 hingga akhir array

Baris 3: Menyimpan nilai sementara dari elemen yang akan dibandingkan

Baris 4: Menentukan indeks sebelumnya untuk dibandingkan

Baris 5: Perulangan untuk membandingkan elemen sebelumnya dengan nilai sementara

Baris 6: Menggeser elemen ke kanan jika lebih besar dari nilai sementara

Baris 7: Mengurangi indeks untuk melanjutkan perbandingan

Baris 8: Menempatkan nilai sementara pada posisi yang benar

Baris 11: Mendefinisikan fungsi utama main()

Baris 12–16: Input jumlah barang dengan validasi error

Baris 17: Membuat list kosong untuk menyimpan data

Baris 18: Menampilkan instruksi input harga barang

Baris 19: Perulangan untuk input sejumlah data

Baris 20–26: Validasi input agar hanya menerima angka

Baris 22: Menambahkan nilai ke dalam list

Baris 27: Menampilkan data sebelum diurutkan

Baris 28: Memanggil fungsi insertion sort

Baris 29: Menampilkan teks hasil pengurutan

Baris 30–31: Menampilkan data yang sudah diurutkan satu per satu

Baris 32: Pindah ke baris baru

Baris 35–36: Menjalankan fungsi main() saat program dieksekusi

## Output Program

<img width="497" height="134" alt="Output" src="https://github.com/user-attachments/assets/5a76386e-5de5-4687-a5f8-0f7330df4374" />

Output program menunjukkan proses pengurutan harga barang menggunakan algoritma Insertion Sort. Pengguna memasukkan jumlah barang sebanyak 5, kemudian memasukkan masing-masing harga yaitu 72000, 64000, 68000, 23000, dan 6500. Program terlebih dahulu menampilkan data sebelum diurutkan dalam bentuk list, yaitu [72000, 64000, 68000, 23000, 6500].

Setelah itu, algoritma Insertion Sort bekerja dengan membandingkan dan memindahkan elemen hingga tersusun secara terurut. Hasil akhirnya ditampilkan dalam urutan ascending, yaitu 6500 23000 64000 68000 72000. Hal ini menunjukkan bahwa program berhasil mengurutkan data dengan benar tanpa error sesuai dengan konsep algoritma yang digunakan.

## Link YouTube


