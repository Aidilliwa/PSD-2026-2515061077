class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                current.value = value
                return
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next

                return True

            prev = current
            current = current.next

        return False

    def display(self):
        print("\nData Kendaraan Parkir dalam Hash Table:")
        for i in range(self.SIZE):
            print(f"{i}: ", end="")
            current = self.table[i]

            while current is not None:
                print(f"(Tiket: {current.key}, Plat: {current.value}) -> ", end="")
                current = current.next

            print("NULL")


def main():
    hashmap = HashMapSeparateChaining()

    # Data kendaraan yang masuk area parkir
    hashmap.insert(101, "BE2515XLD")
    hashmap.insert(111, "BE1077VRS")
    hashmap.insert(121, "BE6090KGH")
    hashmap.insert(102, "BE3553FNE")

    hashmap.display()

    # Mencari kendaraan berdasarkan nomor tiket
    hasil = hashmap.search(111)

    if hasil is not None:
        print(f"\nTiket parkir 111 ditemukan dengan plat nomor = {hasil.value}")
    else:
        print("\nTiket parkir 111 tidak ditemukan")

    # Menghapus kendaraan yang keluar parkir
    hashmap.remove_key(111)

    print("\nSetelah kendaraan dengan tiket 111 keluar parkir:")
    hashmap.display()


if __name__ == "__main__":
    main()