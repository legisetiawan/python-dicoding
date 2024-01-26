# import numpy untuk data matriks memiliki penyimpanan memori yg efisien
import numpy
import os
import sys

var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriks = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
os.system("cls")
# print("Ukuran keseluruhan elemen list dalam bytes( NOTE : 1 bytes terdiri dari 8 bit bil binary 1,0) = ",sys.getsizeof(var_list)*len(var_list))
# print("Ukuran keseluruhan elemen NumPy dalam bytes( NOTE : 1 bytes terdiri dari 8 bit bil binary 1,0) = ", matriks.size*matriks.itemsize)

# matriks pada python deklarasi dan inisialisasi lansung
matrik = [[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1]] # matrik satuan benilai 1 dan 0. ini terdiri dari 3 baris 5 column.
matri = [[0 for i in range(4)] for j in range(3)] # perhatikan tanda siku []. terdiri daru 3 baris 4 column
print(matrik)
print(matri)