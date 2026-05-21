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

Baris 1: Membuat class Node sebagai representasi node pada BST

Baris 2: Membuat constructor __init__

Baris 3: Menyimpan nilai key pada node

Baris 4: Inisialisasi child kiri dengan None

Baris 5: Inisialisasi child kanan dengan None

Baris 8: Membuat class BSTLanjut

Baris 9: Constructor class BST

Baris 10: Inisialisasi root BST dengan None

Baris 12: Membuat fungsi insert node

Baris 13: Jika root kosong maka membuat node baru

Baris 15–16: Jika key lebih kecil, masuk ke subtree kiri

Baris 18–19: Jika key lebih besar, masuk ke subtree kanan

Baris 21: Mengembalikan root

Baris 23–24: Fungsi insert untuk memanggil insert_node

Baris 26: Fungsi mencari node terkecil

Baris 27: Menyimpan root sementara ke current

Baris 29–30: Bergerak ke child kiri sampai node terkecil ditemukan

Baris 32: Mengembalikan node terkecil

Baris 34: Fungsi delete node

Baris 35–36: Jika root kosong, return None

Baris 38–39: Jika key lebih kecil, cari di subtree kiri

Baris 41–42: Jika key lebih besar, cari di subtree kanan

Baris 44: Jika key ditemukan

Baris 45–46: Jika node tidak punya child, hapus node

Baris 48–49: Jika hanya punya child kanan

Baris 51–52: Jika hanya punya child kiri

Baris 54–57: Jika punya dua child, gunakan successor

Baris 59: Mengembalikan root

Baris 61–62: Fungsi delete memanggil delete_node

Baris 64: Fungsi traversal level-order

Baris 65–67: Jika BST kosong tampilkan pesan kosong

Baris 69–70: Membuat queue dan memasukkan root

Baris 72: Perulangan selama queue tidak kosong

Baris 73: Mengambil node pertama dari queue

Baris 75: Menampilkan nilai node

Baris 77–78: Menambahkan child kiri ke queue

Baris 80–81: Menambahkan child kanan ke queue

Baris 83: Pindah baris

Baris 85: Fungsi mencari successor

Baris 86–87: Inisialisasi current dan successor

Baris 89–98: Proses pencarian successor

Baris 100–101: Jika node tidak ditemukan

Baris 103–104: Jika ada subtree kanan, cari nilai terkecil

Baris 106–107: Jika successor tidak ada

Baris 109: Mengembalikan successor

Baris 111: Fungsi mencari predecessor

Baris 112–113: Inisialisasi current dan predecessor

Baris 115–124: Proses pencarian predecessor

Baris 126–127: Jika node tidak ditemukan

Baris 129–135: Jika ada subtree kiri, cari nilai terbesar

Baris 137–138: Jika predecessor tidak ada

Baris 140: Mengembalikan predecessor

Baris 143: Membuat fungsi utama main()

Baris 144: Membuat objek BST

Baris 145: Inisialisasi variabel pilihan menu

Baris 147–153: Menampilkan menu program

Baris 155–159: Input pilihan menu dengan validasi error

Baris 161–167: Menu menambahkan skor player

Baris 169–175: Menu menghapus skor player

Baris 177–178: Menampilkan data level-order

Baris 180–192: Mencari successor suatu skor

Baris 194–206: Mencari predecessor suatu skor

Baris 208–209: Menampilkan pesan program selesai

Baris 211: Menampilkan pesan jika pilihan tidak valid

Baris 214: Mengecek apakah file dijalankan langsung

Baris 215: Memanggil fungsi main()

## Output Program



## Link YouTube


