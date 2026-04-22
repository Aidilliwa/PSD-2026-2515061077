class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.start = None
        self.rear = None

    def create_new_node(self, n):
        new_node = Node(n)
        return new_node

    def insert_node(self, new_node):
        if self.start is None:
            self.start = new_node
            self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node

    def traverse_forward(self):
        print("Playlist dari awal: ", end="")
        current = self.start
        while current is not None:
            print(current.data, end=" | ")
            current = current.next
        print()

    def traverse_backward(self):
        print("Playlist dari akhir: ", end="")
        current = self.rear
        while current is not None:
            print(current.data, end=" | ")
            current = current.prev
        print()

def main():
    dll = DoublyLinkedList()
    choice = 'y'
    while choice.lower() == 'y':
        try:
            c = input("Masukkan judul lagu = ")
        except ValueError:
            print("Masukkan judul lagu yang valid!")
            continue

        print("Menambahkan lagu ke playlist...")
        new_node = dll.create_new_node(c)

        if new_node is not None:
            print("Lagu berhasil ditambahkan")
        else:
            print("Gagal menambahkan lagu")
            break

        dll.insert_node(new_node)
        print("Lagu masuk ke playlist")

        choice = input("Tambah lagu lagi? (y/n) ")

    print("\n=== MENU PLAYLIST ===")
    print("1. Lihat playlist dari awal")
    print("2. Lihat playlist dari akhir")

    try:
        direction = int(input("Pilih tampilan playlist: "))
    except ValueError:
        direction = 1

    if direction == 1:
        dll.traverse_forward()
    elif direction == 2:
        dll.traverse_backward()
    else:
        print("Pilihan tidak valid, menampilkan dari awal")
        dll.traverse_forward()

    print("\nPlaylist selesai ditampilkan. Selamat menikmati musik!")
    print("Program selesai.")

if __name__ == "__main__":
    main()