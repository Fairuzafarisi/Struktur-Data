import os

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def length(self):
        return self.size

    def add_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.size += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.size += 1

    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.size += 1
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            self.size += 1

    def add_after(self, data, value):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.size += 1
            return 
        else:
            current = self.head
            while current is not None: 
                if current.data == value:
                    new_node.next = current.next
                    current.next = new_node
                    self.size += 1
                    return
                current = current.next

    def display(self):
        if self.is_empty():
            print("Linked list kosong.")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next
            print()

    def search_node(self, data):
        if self.is_empty():
            print("Linked list kosong.")
            return False
        
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            else:
                current = current.next
        return False

    def delete_first(self):
        current = self.head
        if self.is_empty():
            print("linked list is empty. Deletion failed.")
            return None
        else:
            self.head = current.next
            self.size -= 1
            return current.data # mengembalikan data yang dihapus

    def delete_last(self):
        if self.is_empty():
            print("linked list is empty. Deletion failed.")
            return None
        
        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            self.size -= 1
            return deleted_data
            
        temp = self.head
        prev = None
        while temp.next is not None:
            prev = temp
            temp = temp.next
            
        deleted_data = temp.data
        prev.next = None
        self.size -= 1
        return deleted_data # mengembalikan data yang dihapus

    def delete_node(self, data):
        # jika data kosong (list empty)
        if self.is_empty():
            print("linked list is empty. Deletion failed.")
            return
        
        # jika data di head
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            print(f"Node with data ({data}) is deleted.")
            return

        current = self.head
        prev = None
        while current is not None and current.data != data:
            prev = current
            current = current.next

        if current is None:
            print(f"Node with data ({data}) not found.")
            return
        
        # Node ditemukan
        prev.next = current.next
        self.size -= 1
        print(f"Node with data ({data}) is deleted.")


my_list = LinkedList()
cek = True

while cek:
    print('-----------Masukkan Pilihan anda-----------')
    print('1. Tambah Elemen pada Linked List')
    print('2. Tampil Elemen dalam Linked List')
    print('3. Hapus Elemen dalam Linked List')
    print('4. Jumlah Elemen dalam Linked List')
    print('0. Keluar')
    
    pil = int(input('Masukkan Pilihan anda: '))
    
    if pil == 1:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        
        temp = True
        while temp:
            print('-----------Pilihan Tambah Data-----------')
            print('1. Tambah Elemen di Awal Linked List')
            print('2. Tambah Elemen di Tengah Linked List')
            print('3. Tambah Elemen di Akhir Linked List')
            print('0. Kembali ke Menu Utama')
            
            pilmenu = int(input('Masukkan Pilihan anda: '))
            
            if pilmenu == 1:
                data = input('Masukkan Data yang ingin ditambahkan: ')
                my_list.add_first(data)
                print(f'Data ({data}) berhasil ditambahkan di awal linked list')
            elif pilmenu == 2:
                data = input('Masukkan Data yang ingin ditambahkan: ')
                value = input('Data ingin ditambahkan setelah data apa?: ')
                my_list.add_after(data, value)
                print(f'Data ({data}) berhasil ditambahkan setelah ({value})')
            elif pilmenu == 3:
                data = input('Masukkan Data yang ingin ditambahkan: ')
                my_list.add_last(data)
                print(f'Data ({data}) berhasil ditambahkan di akhir linked list')
            elif pilmenu == 0:
                temp = False
                break
    
    elif pil == 2:
        my_list.display()
        
    elif pil == 3:
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        
        temp = True
        while temp:
            print('-----------Pilihan Hapus Data-----------')
            print('1. Hapus Elemen di Awal Linked List')
            print('2. Hapus Elemen di Tengah Linked List')
            print('3. Hapus Elemen di Akhir Linked List')
            print('0. Kembali ke Menu Utama')
            
            pilmenu = int(input('Masukkan Pilihan anda: '))
            
            if pilmenu == 1:
                hapus = my_list.delete_first()
                if hapus is not None:
                    print(f'Data ({hapus}) berhasil dihapus')
            elif pilmenu == 2:
                data = input('Masukkan Data yang ingin dihapus: ')
                my_list.delete_node(data)
            elif pilmenu == 3:
                hapus = my_list.delete_last()
                if hapus is not None:
                    print(f'Data ({hapus}) berhasil dihapus')
            elif pilmenu == 0:
                temp = False
                break
                
    elif pil == 4:
        print(f'Jumlah node dalam linked list: {my_list.length()}')
        
    elif pil == 0:
        print('Bye..!!!')
        cek = False
        break
        
    else:
        print('Pilihan tidak ada!')