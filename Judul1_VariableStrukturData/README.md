# Simulasi Playlist Lagu Menggunakan Double Linked List

Program ini merupakan simulasi sederhana dari playlist lagu seperti yang terdapat pada aplikasi pemutar musik. Pengguna dapat memasukkan beberapa judul lagu, kemudian menampilkan daftar lagu tersebut dari awal maupun akhir.

Struktur data yang digunakan dalam program ini adalah Double Linked List, di mana setiap node memiliki dua pointer, yaitu next (menuju node berikutnya) dan prev (menuju node sebelumnya). Dengan struktur ini, data dapat ditelusuri secara dua arah (maju dan mundur), sehingga cocok digunakan untuk playlist lagu.

---

## Source Code

![Source Code 1](https://github.com/Aidilliwa/PSD-2026-2515061077/blob/main/Judul1_VariableStrukturData/Source%20Code%201.png?raw=true)

![Source Code 2](https://github.com/Aidilliwa/PSD-2026-2515061077/blob/main/Judul1_VariableStrukturData/Source%20Code%202.png?raw=true)

Baris 1: Membuat class Node (representasi 1 lagu)

Baris 2: Mendefinisikan konstruktor saat node dibuat

Baris 3: Menyimpan data (judul lagu) ke dalam node

Baris 4: Inisialisasi pointer ke node sebelumnya (prev = None)

Baris 5: Inisialisasi pointer ke node berikutnya (next = None)

Baris 7: Membuat class DoublyLinkedList (struktur playlist)

Baris 8: Mendefinisikan konstruktor class

Baris 9: Inisialisasi pointer ke node pertama (start = None)

Baris 10: Inisialisasi pointer ke node terakhir (rear = None)

Baris 12: Mendefinisikan fungsi untuk membuat node baru

Baris 13: Membuat objek node dengan data yang diberikan

Baris 14: Mengembalikan node yang telah dibuat

Baris 16: Mendefinisikan fungsi untuk menambahkan node ke list

Baris 17: Mengecek apakah list masih kosong

Baris 18: Jika kosong, node menjadi node pertama

Baris 19: Node juga menjadi node terakhir

Baris 20: Jika list tidak kosong, masuk ke kondisi else

Baris 21: Menghubungkan node baru ke node terakhir sebelumnya

Baris 22: Node terakhir sebelumnya menunjuk ke node baru

Baris 23: Memperbarui node terakhir menjadi node baru

Baris 25: Mendefinisikan fungsi traversal maju

Baris 26: Menampilkan teks “Playlist dari awal”

Baris 27: Mengatur pointer mulai dari node pertama

Baris 28: Perulangan selama node masih ada

Baris 29: Menampilkan data pada node saat ini

Baris 30: Berpindah ke node berikutnya

Baris 31: Pindah ke baris baru setelah selesai

Baris 33: Mendefinisikan fungsi traversal mundur

Baris 34: Menampilkan teks “Playlist dari akhir”

Baris 35: Mengatur pointer mulai dari node terakhir

Baris 36: Perulangan selama node masih ada

Baris 37: Menampilkan data pada node saat ini

Baris 38: Berpindah ke node sebelumnya

Baris 39: Pindah ke baris baru setelah selesai

Baris 41: Mendefinisikan fungsi utama main()

Baris 42: Membuat objek DoublyLinkedList

Baris 43: Inisialisasi variabel kontrol perulangan (choice = 'y')

Baris 44: Memulai perulangan selama user memilih ‘y’

Baris 45: Memulai blok try

Baris 46: Input judul lagu dari user

Baris 47: Menangani error jika input tidak valid

Baris 48: Menampilkan pesan kesalahan

Baris 49: Melanjutkan ke iterasi berikutnya

Baris 51: Menampilkan proses penambahan lagu

Baris 52: Membuat node baru dari input user

Baris 54: Mengecek apakah node berhasil dibuat

Baris 55: Jika berhasil, tampilkan pesan sukses

Baris 56: Jika gagal, masuk ke kondisi else

Baris 57: Menampilkan pesan gagal

Baris 58: Menghentikan perulangan

Baris 60: Memasukkan node ke dalam linked list

Baris 61: Menampilkan konfirmasi lagu berhasil dimasukkan

Baris 63: Menanyakan apakah user ingin menambah lagu lagi

Baris 65: Menampilkan judul menu playlist

Baris 66: Menampilkan opsi melihat dari awal

Baris 67: Menampilkan opsi melihat dari akhir

Baris 69: Memulai blok try untuk input pilihan

Baris 70: Input pilihan tampilan dari user

Baris 71: Menangani error jika input tidak valid

Baris 72: Default pilihan menjadi 1

Baris 74: Jika user memilih 1

Baris 75: Menampilkan playlist dari awal

Baris 76: Jika user memilih 2

Baris 77: Menampilkan playlist dari akhir

Baris 78: Jika pilihan tidak valid

Baris 79: Menampilkan pesan kesalahan

Baris 80: Menampilkan playlist dari awal

Baris 82: Menampilkan pesan bahwa playlist selesai ditampilkan

Baris 83: Menampilkan pesan program selesai

Baris 85: Mengecek apakah file dijalankan sebagai program utama

Baris 86: Memanggil fungsi main()

## Output Program

![Output](https://github.com/Aidilliwa/PSD-2026-2515061077/blob/main/Judul1_VariableStrukturData/Output.png?raw=true)

Output program menunjukkan proses pembuatan dan penampilan playlist lagu menggunakan struktur Double Linked List. Pengguna memasukkan beberapa judul lagu seperti Viva La Vida, Payphone, Ghost, dan Sunflower, di mana setiap input akan dibuat menjadi node baru dan ditambahkan ke dalam list secara berurutan di bagian akhir. 

Selama pengguna memilih “y”, program terus menerima input lagu, dan berhenti ketika memilih “n”. Setelah itu, program menampilkan menu pilihan untuk melihat playlist dari awal atau akhir. Pada contoh ini, pengguna memilih opsi 1 sehingga program menampilkan playlist dari awal menggunakan traversal maju (forward), yaitu sesuai urutan input: Viva La Vida | Payphone | Ghost | Sunflower. 

Terakhir, program menampilkan pesan bahwa playlist selesai ditampilkan dan program berakhir tanpa error, yang menandakan bahwa seluruh proses berjalan dengan baik sesuai studi kasus.

## Link YouTube

https://youtu.be/3uGMV1OeyhU
