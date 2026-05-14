class StackArray:
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, x):
        if self.is_full():
            print("Riwayat file penuh")
            return
        self.top_idx += 1
        self.st[self.top_idx] = x
        print(f"File '{x}' berhasil dibuka")

    def pop(self):
        if self.is_empty():
            print("Tidak ada riwayat file")
            return
        print(f"File terakhir '{self.st[self.top_idx]}' berhasil ditutup")
        self.top_idx -= 1

    def peek(self):
        if self.is_empty():
            print("Tidak ada file yang sedang dibuka")
            return
        print(f"File terakhir dibuka: {self.st[self.top_idx]}")

    def display(self):
        if self.is_empty():
            print("Riwayat file kosong")
            return
        print("Riwayat file (terbaru ke terlama): ", end="")
        for i in range(self.top_idx, -1, -1):
            print(self.st[i], end=" | ")
        print()


def main():
    stack = StackArray()
    pilih = 0

    while pilih != 5:
        print("\n=== RIWAYAT FILE ===")
        print("1. Buka File")
        print("2. Tutup File")
        print("3. Lihat File Terakhir")
        print("4. Tampilkan Riwayat File")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input tidak valid!")
            continue

        if pilih == 1:
            try:
                val = input("Masukkan nama file: ")
                stack.push(val)
            except ValueError:
                print("Input tidak valid!")

        elif pilih == 2:
            stack.pop()

        elif pilih == 3:
            stack.peek()

        elif pilih == 4:
            stack.display()

        elif pilih == 5:
            print("Program selesai.")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()