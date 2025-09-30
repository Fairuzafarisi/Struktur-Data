class Queue:
    # method wadah data
    def __init__(self): #__init__ = Constructor 
        self.qlist = list()

    # method cek is_empty
    def is_empty(self):
        return len(self) == 0
    
    # method berapa banyak elemen di dalam objek
    def __len__(self):
        return len(self.qlist)
    
    # method enqueue
    def enqueue(self, data):
        self.qlist.append(data)

    # method dequeue
    def dequeue(self):
        if self.is_empty():
            print('Queue kososng. Tidak ada data yang dapat di dequeu.')
        else:
            return self.qlist.pop(0)
    
    # method untuk menunjukkan isi antrian (queue) ke layar
    def display(self):
        if self.is_empty():
            print('Queue kososng. Tidak ada data yang dapat di ditampilkan.')
        else:
            for item in self.qlist:
                print(item, end='')
    
    # method untuk Menghapus seluruh elemen queue sampai kosong
    def delete_all(self):
        while not self.is_empty():
            self.dequeue()

#Create Queue
myQueue = Queue()

cek = True

while cek:
    print()
    print('-------Masukkan Pilihan Anda-------')
    print('1. Tambah elemen pada queue')
    print('2. Tampil elemen pada queue')
    print('3. Hapus elemen pada queue')
    print('4. Hapus seluruh data pada queue')
    print('-----------------------------------')
    print('0. Keluar')
    print()

    pil = int(input('Masukkan pilihan anda: '))

    if pil == 1:
        jum = int(input('Masukkan jumlah data: '))

        if jum > 0:
            i = 1
            while i <= jum:
                data = input('Masukkan data ingin diinput: ')
                myQueue.enqueue(data)
                i+=1
        else:
            print('Jumlah data minimal 1!!')
    
    elif pil == 2:
        print('Isi Queue: ')
        myQueue.display()
    
    elif pil == 3:
        myQueue.dequeue()
    
    elif pil == 4:
        myQueue.delete_all()
    
    elif pil == 0:
        print('Bye trooopres....\n')
        pil = False
        break

    else:
        print('Pilihan tidak ada')