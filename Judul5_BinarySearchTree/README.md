# Manajemen Data Skor Player Menggunakan Binary Search Tree (BST)

Program ini untuk mengelola data skor player pada sebuah game menggunakan struktur data Binary Search Tree (BST). Pengguna dapat menambahkan skor player, menghapus skor, menampilkan data skor secara level-order, serta mencari skor setelahnya (successor) dan skor sebelumnya (predecessor).

Struktur data yang digunakan adalah Binary Search Tree (BST), yaitu struktur data berbentuk pohon biner yang memiliki aturan bahwa nilai di sebelah kiri lebih kecil dari root, sedangkan nilai di sebelah kanan lebih besar dari root. BST memudahkan proses pencarian, penambahan, dan penghapusan data dengan lebih terstruktur dan efisien dibanding pencarian biasa.

---

## Source Code

<img width="529" height="916" alt="Source Code 1" src="https://github.com/user-attachments/assets/f1c3a729-5f21-43b8-af0e-f87249892647" />

<img width="597" height="916" alt="Source Code 2" src="https://github.com/user-attachments/assets/e0c0b2f5-4120-49a4-ab16-845fc995e73d" />

<img width="518" height="916" alt="Source Code 3" src="https://github.com/user-attachments/assets/dedfcbb4-77e6-4455-83a4-2dd41c620e6b" />

<img width="530" height="917" alt="Source Code 4" src="https://github.com/user-attachments/assets/287ef32e-d702-4492-b3b0-fc407c3c0ea1" />

<img width="534" height="406" alt="Source Code 5" src="https://github.com/user-attachments/assets/a3be58fb-8923-4942-a4d5-7ff97d46f1a0" />

Baris 1: Mendefinisikan kelas bernama Node.

Baris 2: Membuat konstruktor __init__ yang otomatis berjalan saat objek Node baru dibuat dengan menerima parameter nilai skor (key).

Baris 3: Menyimpan nilai skor input ke dalam variabel objek self.key.

Baris 4: Membuat pointer self.left bernilai None untuk menunjuk ke anak sebelah kiri.

Baris 5: Membuat pointer self.right bernilai None untuk menunjuk ke anak sebelah kanan.

Baris 8: Mendefinisikan kelas utama bernama BSTLanjut.

Baris 9: Membuat fungsi konstruktor objek untuk struktur pohon utama.

Baris 10: Menginisialisasi akar pohon (self.root) dengan nilai awal None (pohon kosong).

Baris 12: Membuat fungsi pembantu rekursif insert_node untuk mencari posisi input data baru berdasarkan node saat ini.

Baris 13: Memeriksa apakah posisi node saat ini kosong (None).

Baris 14: Jika kosong, mengembalikan objek Node baru sebagai tempat penyimpanan skor.

Baris 16: Memeriksa apakah skor baru lebih kecil dari skor node saat ini.

Baris 17: Jika lebih kecil, program bergerak ke kiri secara rekursif dan hasilnya dihubungkan ke pointer anak kiri.

Baris 19: Memeriksa apakah skor baru lebih besar dari skor node saat ini.

Baris 20: Jika lebih besar, program bergerak ke kanan secara rekursif dan hasilnya dihubungkan ke pointer anak kanan.

Baris 22: Mengembalikan posisi node saat ini agar struktur pohon di atasnya tetap terhubung.

Baris 24: Membuat fungsi publik insert untuk dipanggil dari luar kelas.

Baris 25: Menjalankan proses penambahan data dengan memperbarui self.root utama melalui fungsi insert_node.

Baris 27: Membuat fungsi find_min_node untuk mencari nilai terkecil pada suatu sub-pohon.

Baris 28: Menetapkan node awal pencarian ke dalam variabel penanda current.

Baris 30: Melakukan perulangan selama anak kiri dari node saat ini masih tersedia.

Baris 31: Menggeser posisi current terus ke arah anak sebelah kiri.

Baris 33: Mengembalikan node paling kiri (nilai terkecil) yang berhasil ditemukan.

Baris 35: Membuat fungsi pembantu rekursif delete_node untuk menghapus skor tertentu.

Baris 36: Memeriksa apakah node yang diperiksa kosong (None).

Baris 37: Jika kosong, mengembalikan nilai None karena skor tidak ditemukan.

Baris 39: Memeriksa apakah skor yang ingin dihapus lebih kecil dari skor node saat ini.

Baris 40: Jika lebih kecil, program melakukan rekursi mencari data ke arah sub-pohon kiri.

Baris 42: Memeriksa apakah skor yang ingin dihapus lebih besar dari skor node saat ini.

Baris 43: Jika lebih besar, program melakukan rekursi mencari data ke arah sub-pohon kanan.

Baris 45: Blok alternatif jika skor yang dicari cocok dengan skor node saat ini (data ditemukan).

Baris 46: Memeriksa apakah node target tidak memiliki anak sama sekali (node daun).

Baris 47: Jika benar daun, hapus node dengan mengembalikan nilai None.

Baris 49: Memeriksa apakah node target hanya tidak memiliki anak kiri (hanya punya anak kanan).

Baris 50: Menggantikan posisi node saat ini dengan anak kanannya tersebut.

Baris 52: Memeriksa apakah node target hanya tidak memiliki anak kanan (hanya punya anak kiri).

Baris 53: Menggantikan posisi node saat ini dengan anak kirinya tersebut.

Baris 55: Blok alternatif jika node yang dihapus memiliki dua anak sekaligus.

Baris 56: Mencari nilai pengganti terdekat menggunakan nilai minimum dari sub-pohon kanan (successor).

Baris 57: Mengganti nilai skor node saat ini dengan nilai dari node successor.

Baris 58: Menghapus node successor yang asli di sub-pohon kanan secara rekursif agar tidak ganda.

Baris 60: Mengembalikan struktur node saat ini yang telah diperbarui.

Baris 62: Membuat fungsi publik delete untuk menghapus skor dari luar kelas.

Baris 63: Memperbarui struktur self.root utama dengan memanggil fungsi delete_node.

Baris 65: Membuat fungsi level_order untuk mencetak isi pohon per level secara horizontal.

Baris 66: Memeriksa apakah kondisi pohon dalam keadaan kosong.

Baris 67: Jika kosong, mencetak teks "(kosong)" ke layar.

Baris 68: Keluar secara paksa dari fungsi karena tidak ada data yang bisa diproses.

Baris 70: Membuat list kosong bernama queue untuk digunakan sebagai struktur data antrean.

Baris 71: Memasukkan node paling atas (root) sebagai elemen pertama di dalam antrean.

Baris 73: Melakukan perulangan selama antrean queue masih memiliki elemen di dalamnya.

Baris 74: Mengambil sekaligus menghapus elemen terdepan (indeks 0) dari antrean ke variabel current.

Baris 76: Mencetak skor dari node yang diambil ke layar dengan pemisah karakter spasi.

Baris 78: Memeriksa apakah node saat ini memiliki anak di sebelah kiri.

Baris 79: Jika ada, masukkan anak kiri tersebut ke baris antrean paling belakang.

Baris 81: Memeriksa apakah node saat ini memiliki anak di sebelah kanan.

Baris 82: Jika ada, masukkan anak kanan tersebut ke baris antrean paling belakang.

Baris 84: Mencetak baris baru di akhir penelusuran agar tampilan output rapi.

Baris 86: Membuat fungsi find_successor untuk mencari nilai terkecil setelah skor target.

Baris 87: Menetapkan penanda current mulai berjalan dari posisi root pohon.

Baris 88: Menyiapkan variabel penampung hasil bernama successor dengan nilai awal None.

Baris 90: Melakukan perulangan pencarian selama node current tidak bernilai kosong.

Baris 91: Memeriksa apakah skor target lebih kecil dari nilai skor node saat ini.

Baris 92: Jika lebih kecil, node saat ini disimpan sebagai kandidat sementara untuk nilai successor.

Baris 93: Menggeser pointer current ke sub-pohon kiri untuk mencari nilai yang lebih kecil lagi.

Baris 95: Memeriksa apakah skor target lebih besar dari nilai skor node saat ini.

Baris 96: Jika lebih besar, langsung menggeser pointer current ke sub-pohon kanan.

Baris 98: Blok alternatif jika skor target sama dengan nilai skor node saat ini (target ketemu).

Baris 99: Menghentikan perulangan penelusuran pohon secara paksa.

Baris 101: Memeriksa apakah setelah loop selesai posisi current berakhir kosong.

Baris 102: Jika kosong (target tidak ada di pohon), mengembalikan nilai None dan status False.

Baris 104: Memeriksa apakah node target yang ditemukan memiliki sub-pohon di sebelah kanan.

Baris 105: Jika ada, nilai successor sejati diambil dari nilai minimum di sub-pohon kanan tersebut.

Baris 107: Memeriksa apakah variabel hasil successor masih tetap bernilai kosong.

Baris 108: Jika tetap kosong, mengembalikan nilai None dan status False (tidak memiliki successor).

Baris 110: Mengembalikan data nilai skor dari successor beserta status keberhasilan True.

Baris 112: Membuat fungsi find_predecessor untuk mencari nilai terbesar sebelum skor target.

Baris 113: Menetapkan penanda current mulai berjalan dari posisi root pohon.

Baris 114: Menyiapkan variabel penampung hasil bernama predecessor dengan nilai awal None.

Baris 116: Melakukan perulangan pencarian selama node current tidak bernilai kosong.

Baris 117: Memeriksa apakah skor target lebih besar dari nilai skor node saat ini.

Baris 118: Jika lebih besar, node saat ini disimpan sebagai kandidat sementara untuk nilai predecessor.

Baris 119: Menggeser pointer current ke sub-pohon kanan untuk mencari nilai yang lebih besar lagi.

Baris 121: Memeriksa apakah skor target lebih kecil dari nilai skor node saat ini.

Baris 122: Jika lebih kecil, langsung menggeser pointer current ke sub-pohon kiri.

Baris 124: Blok alternatif jika skor target sama dengan nilai skor node saat ini.

Baris 125: Menghentikan perulangan penelusuran pohon secara paksa.

Baris 127: Memeriksa apakah setelah loop selesai posisi current berakhir kosong.

Baris 128: Jika kosong (target tidak ada di pohon), mengembalikan nilai None dan status False.

Baris 130: Memeriksa apakah node target yang ditemukan memiliki sub-pohon di sebelah kiri.

Baris 131: Membuat pointer penjelajah sementara bernama temp di posisi anak kiri target.

Baris 133: Melakukan perulangan geser ke kanan selama anak kanan dari temp masih tersedia.

Baris 134: Menggeser posisi pointer temp ke arah anak sebelah kanan.

Baris 136: Menetapkan posisi paling kanan tersebut sebagai objek hasil predecessor yang sejati.

Baris 138: Memeriksa apakah variabel hasil predecessor masih tetap bernilai kosong.

Baris 139: Jika tetap kosong, mengembalikan nilai None dan status False (tidak memiliki predecessor).

Baris 141: Mengembalikan data nilai skor dari predecessor beserta status keberhasilan True.

Baris 144: Mendefinisikan fungsi utama bernama main.

Baris 145: Membuat objek pohon baru bernama bst dari cetakan kelas BSTLanjut.

Baris 146: Membuat variabel pilih dengan nilai awal 0 untuk menampung pilihan menu pengguna.

Baris 148: Melakukan perulangan program selama nilai opsi menu yang dipilih bukan angka 6.

Baris 149 sampai 155: Mencetak daftar teks menu pilihan 1 sampai 6 ke layar terminal komputer.

Baris 157: Membuka blok penanganan kesalahan input menu utama.

Baris 158: Mengambil data input pilihan pengguna dan mengubah formatnya menjadi bilangan bulat (int).

Baris 160: Blok penangkap kesalahan tipe data input jika pengguna memasukkan selain angka asli.

Baris 161: Mencetak teks informasi peringatan bahwa data "Input tidak valid!".

Baris 162: Mengabaikan perintah sisa dan melompat kembali ke awal perulangan menu utama.

Baris 164: Memeriksa apakah pengguna memilih nomor menu 1 (Tambah Skor).

Baris 165: Membuka blok proteksi kesalahan data untuk input penambahan skor.

Baris 166: Meminta pengguna memasukkan nilai skor dalam format bilangan bulat ke variabel x.

Baris 167: Memasukkan nilai skor x ke dalam sistem pohon lewat perintah fungsi bst.insert.

Baris 168: Mencetak pesan konfirmasi bahwa data skor sukses dimasukkan ke dalam sistem.

Baris 169: Menangkap kesalahan input jika pengguna tidak memasukkan angka bulat yang benar.

Baris 170: Mencetak pemberitahuan peringatan bahwa input tidak valid.

Baris 173: Memeriksa apakah pengguna memilih nomor menu 2 (Hapus Skor).

Baris 174: Membuka blok proteksi kesalahan data untuk input penghapusan skor.

Baris 175: Meminta pengguna memasukkan nilai skor yang akan dihapus dari sistem ke variabel x.

Baris 176: Menghapus data skor x di dalam pohon menggunakan perintah fungsi bst.delete.

Baris 177: Mencetak pesan konfirmasi sukses bahwa data skor telah dibersihkan dari sistem.

Baris 178: Menangkap kesalahan input jika data yang dimasukkan salah tipe.

Baris 179: Mencetak pemberitahuan peringatan kesalahan input ke layar.

Baris 182: Memeriksa apakah pengguna memilih nomor menu 3 (Tampilkan Data).

Baris 183: Mencetak awalan teks keterangan format cetak data skor.

Baris 184: Memanggil fungsi bst.level_order untuk mencetak seluruh isi pohon terstruktur ke layar.

Baris 186: Memeriksa apakah pengguna memilih nomor menu 4 (Cari Skor Setelahnya).

Baris 187: Membuka blok proteksi kesalahan data untuk menu pencarian successor.

Baris 188: Meminta input skor target pencarian successor dari pengguna ke variabel x.

Baris 189: Menjalankan fungsi bst.find_successor dan hasilnya diurai ke variabel ans dan found.

Baris 191: Memeriksa apakah status variabel status found bernilai sukses (True).

Baris 192: Jika sukses, mencetak hasil nilai skor successor yang dicari ke layar.

Baris 194: Blok alternatif jika data status bernilai gagal atau tidak ditemukan.

Baris 195: Mencetak informasi teks bahwa target "Tidak ada successor".

Baris 197: Menangkap kesalahan input jika pengguna menginputkan nilai non-angka.

Baris 198: Mencetak pemberitahuan peringatan kesalahan input ke layar.

Baris 200: Memeriksa apakah pengguna memilih nomor menu 5 (Cari Skor Sebelumnya).

Baris 201: Membuka blok proteksi kesalahan data untuk menu pencarian predecessor.

Baris 202: Meminta input skor target pencarian predecessor dari pengguna ke variabel x.

Baris 203: Menjalankan fungsi bst.find_predecessor dan hasilnya diurai ke variabel ans dan found.

Baris 205: Memeriksa apakah status variabel status found bernilai sukses (True).

Baris 206: Jika sukses, mencetak hasil nilai skor predecessor yang dicari ke layar.

Baris 208: Blok alternatif jika data status bernilai gagal atau tidak ditemukan.

Baris 209: Mencetak informasi teks bahwa target "Tidak ada predecessor".

Baris 211: Menangkap kesalahan input tipe data pada menu pencarian.

Baris 212: Mencetak pemberitahuan peringatan kesalahan input ke layar.

Baris 214: Memeriksa apakah pengguna memilih nomor menu 6 (Keluar Program).

Baris 215: Mencetak pesan penutup bahwa operasional aplikasi selesai dijalankan.

Baris 217: Blok akhir jika input menu berupa angka di luar jangkauan pilihan yang tersedia (1-6).

Baris 218: Mencetak pesan peringatan "Pilihan tidak valid!".

Baris 221: Memeriksa apakah file script Python ini sedang dijalankan secara langsung sebagai program utama.

Baris 222: Memanggil fungsi main() untuk mulai mengaktifkan seluruh siklus program.

## Output Program



## Link YouTube


