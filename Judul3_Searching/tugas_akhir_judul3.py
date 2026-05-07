def sequential_search(data, n, target):
    i = 0
    counter = 0
    while i < n:
        if data[i] == target:
            counter += 1
        i += 1
    return counter


def main():
    # Data nomor kupon undian peserta
    data = [102, 115, 108, 120, 115, 130, 140, 115, 150]

    n = len(data)

    print("Daftar Nomor Kupon Undian:")
    print(data)

    # Input nomor kupon yang ingin dicari
    while True:
        try:
            target = int(input("Masukkan nomor kupon yang dicari: "))
            break
        except ValueError:
            print("Input harus berupa angka!")

    # Proses pencarian
    counter = sequential_search(data, n, target)

    # Menampilkan hasil
    if counter > 0:
        print(f"Nomor kupon {target} ditemukan sebanyak {counter} kali.")
    else:
        print(f"Nomor kupon {target} tidak ditemukan.")


if __name__ == "__main__":
    main()