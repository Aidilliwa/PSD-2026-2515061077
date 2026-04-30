def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp


def main():
    try:
        n = int(input("Masukkan jumlah barang: "))
    except ValueError:
        print("Input tidak valid!")
        return
    arr = []
    print("Masukkan harga barang:")
    for i in range(n):
        while True:
            try:
                nilai = int(input())
                arr.append(nilai)
                break
            except ValueError: 
                print("Input tidak valid, silakan masukkan angka!")
    print(f"Harga barang sebelum diurutkan: {arr}")
    insertion_sort(arr, n)
    print("Harga barang setelah diurutkan (Insertion Sort):", end=" ")
    for i in range(n):
        print(arr[i], end=" ")
    print()


if __name__ == "__main__":
    main()