
import os


# ----------------------------------------
# NODE CLASS (Representasi satu elemen Linked List)
# ----------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ----------------------------------------
# LINKED LIST CLASS
# ----------------------------------------
class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # Mengecek apakah list kosong
    def is_empty(self):
        return self.head is None

    # Mengembalikan jumlah elemen
    def length(self):
        return self.size

    # Tambah elemen di awal
    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    # Tambah elemen di akhir
    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    # Tambah elemen setelah data tertentu
    def add_after(self, data, value):
        if self.is_empty():
            print("Linked list kosong, data ditambahkan sebagai elemen pertama.")
            self.add_first(data)
            return

        current = self.head
        while current:
            if current.data == value:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                self.size += 1
                return
            current = current.next

        print(f"Data {value} tidak ditemukan, data {data} tidak ditambahkan.")

    # Menampilkan seluruh elemen dalam linked list
    def display(self):
        if self.is_empty():
            print("Linked list kosong.")
        else:
            current = self.head
            while current:
                print(current.data, end=" -> " if current.next else "\n")
                current = current.next

    # Mencari data
    def search_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    # Menghapus elemen pertama
    def delete_first(self):
        if self.is_empty():
            print("Linked list kosong. Deletion failed.")
            return None
        deleted = self.head.data
        self.head = self.head.next
        self.size -= 1
        return deleted

    # Menghapus elemen terakhir
    def delete_last(self):
        if self.is_empty():
            print("Linked list kosong. Deletion failed.")
            return None
        if self.head.next is None:
            deleted = self.head.data
            self.head = None
            self.size -= 1
            return deleted
        current = self.head
        while current.next.next:
            current = current.next
        deleted = current.next.data
        current.next = None
        self.size -= 1
        return deleted

    # Menghapus node berdasarkan data
    def delete_node(self, data):
        if self.is_empty():
            print("Linked list kosong. Deletion failed.")
            return
        if self.head.data == data:
            self.delete_first()
            print(f"Node dengan data {data} telah dihapus.")
            return

        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next is None:
            print(f"Node dengan data {data} tidak ditemukan.")
        else:
            current.next = current.next.next
            self.size -= 1
            print(f"Node dengan data {data} telah dihapus.")


# ----------------------------------------
# PROGRAM UTAMA (MENU INTERAKTIF)
# ----------------------------------------
my_list = LinkedList()
cek = True

while cek:
    print("\n------- Menu Utama -------")
    print("1. Tambah Elemen pada Linked List")
    print("2. Tampil Elemen dalam Linked List")
    print("3. Hapus Elemen dalam Linked List")
    print("4. Jumlah Elemen dalam Linked List")
    print("0. Keluar")
    print("---------------------------")

    pil = input("Masukkan Pilihan Anda: ")

    if pil == "1":
        while True:
            print("\n--- Pilihan Tambah Data ---")
            print("1. Tambah Elemen di Awal Linked List")
            print("2. Tambah Elemen di Tengah (Setelah Data Tertentu)")
            print("3. Tambah Elemen di Akhir Linked List")
            print("0. Kembali ke Menu Utama")
            sub = input("Masukkan Pilihan Anda: ")

            if sub == "1":
                data = input("Masukkan Data: ")
                my_list.add_first(data)
                print(f"Data {data} berhasil ditambahkan di awal.")
            elif sub == "2":
                data = input("Masukkan Data Baru: ")
                value = input("Masukkan Data Setelah Apa: ")
                my_list.add_after(data, value)
            elif sub == "3":
                data = input("Masukkan Data: ")
                my_list.add_last(data)
                print(f"Data {data} berhasil ditambahkan di akhir.")
            elif sub == "0":
                break
            else:
                print("Pilihan tidak valid.")

    elif pil == "2":
        print("\nIsi Linked List:")
        my_list.display()

    elif pil == "3":
        while True:
            print("\n--- Pilihan Hapus Data ---")
            print("1. Hapus Elemen di Awal Linked List")
            print("2. Hapus Elemen Tertentu")
            print("3. Hapus Elemen di Akhir Linked List")
            print("0. Kembali ke Menu Utama")
            sub = input("Masukkan Pilihan Anda: ")

            if sub == "1":
                hapus = my_list.delete_first()
                if hapus:
                    print(f"Data {hapus} berhasil dihapus.")
            elif sub == "2":
                data = input("Masukkan Data yang ingin dihapus: ")
                my_list.delete_node(data)
            elif sub == "3":
                hapus = my_list.delete_last()
                if hapus:
                    print(f"Data {hapus} berhasil dihapus.")
            elif sub == "0":
                break
            else:
                print("Pilihan tidak valid.")

    elif pil == "4":
        print(f"\nJumlah node dalam linked list: {my_list.length()}")

    elif pil == "0":
        print("\nBye... Byee...!!")
        cek = False

    else:
        print("Pilihan tidak ada.")