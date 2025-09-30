import os
from queue import LifoQueue
from collections import deque

print()
MaxSize = int(input('Masukkan jumlah data yang ingin ditambah: '))

DequeStack = deque()
LifoStack = LifoQueue(maxsize = MaxSize) 

cek = True

while cek:
    os.system('cls')
    print('-Masukkan pilihan anda-')
    print('1. Stack dengan Deque')
    print('2. Stack dengan Lifoqueue')
    print('0. Keluar')

    pil = int(input('Masukan Pilihan anda'))

    if pil == 1:
        os.system('cls')
        i = 1
        temp = True
        while temp:
            print()
            print('-Masukan Pilihan anda-')
            print(' 1. Tambah Data dengan Deque')
            print('2. Hapus Data Deque')
            print(' 3. Tampil Data Deque')
            print(' 4. Jumlah Data Deque')
            print('0. Keluar')
            pilMenu = int(input('masukan pilihan anda:'))
            print()
            
            if pilMenu == 1:
                if len(DequeStack) <= MaxSize :
                    while i <= MaxSize:
                        item = input(f'Masukan data ke-{i}: ')
                        DequeStack.append(item)
                        i+=1
                else: 
                    print('Data tidak bisa ditambah. Stack sudah penuh!')
            
            elif pilMenu == 2:
                if len(DequeStack) != 0:
                    print(f'Elemen terakhir: {DequeStack.pop()} telah dihapus')
                else:
                    print('Stack kosong. Tidak ada elemen untuk dihapus!!')

            elif pilMenu == 3:
                print('Data dalam Stack adəlah:') 
                print (DequeStack)

            elif pilMenu == 4:
                print(f'Jumlah Data dalam Stack = {len(DequeStack)}')
            
            else:
                pilMenu = False
                break

    elif pil == 2:

        os.system('cls')
        temp = True
        while temp:
            print()
            print('-Masukan Pilihan anda-')
            print('1. Tambah Data dengan LifoQueue')
            print('2. Hapus Data LifoQueue')
            print('3. Tampil Data LifoQueue')
            print('4. Jumlah Data LifoQuede')
            print('0. Keluar')
            pilMenu = int (input('masukan pilihan anda:'))
            print()

        if pilMenu == 1:
            if LifoStack.qsize()==0:
                i = 1
            else:
                i = LifoStack.qsize()+ 1
            if LifoStack.full() == False:
                while i <= MaxSize:
                    item = input(f'Masukan data ke-{i}: ')
                    LifoStack.put(item)
                    i += 1
                i = 1# reset countor
            else:
                print('Data tidak bisa ditambah. Stack Sudah penuh!')
        
        elif pilMenu == 2:
            if LifoStack.empty() == False: 
                print(f'Elemen terakhir: {LifoStack.get()} telah dihapus')
            else:
                print('Stack kosong. Tidak ada elemen untuk dihapus!!')

        elif pilMenu == 3:
            isi = list(LifoStack.queue)
            print('Data dalam Stack adalah:') 
            print(isi)

        elif pilMenu == 4:
            print(f'Jumlah Data dalam Stack = {LifoStack.qsize()}')

        else:
            pilMenu = False
            break

    elif pil == 0:
        pil= False
        break

    else:
        print('Pilihan tidak ada')