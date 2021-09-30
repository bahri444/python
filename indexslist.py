#himpunan data
#index
#list
b=[1,2,3,4,5,6,7,8,9,10,15,16,18,20,31]
print(b[-4:])#menampilkan angka 4 terakhir dari angka 16-31
print(b[:3])#menampilkan data tiga angka di awal
print(b[4:-7])#menampilkan 4 angka di tengah
print(b[8:-3])#menampilkan angka 9 sampai 16

b=[1,2,3,4,5,6,7,8,9,10,15,16,18,20,31]
b[11:]=[21,22,23,24]#mengganti angka 4 terakhir dari angka 16-31
print(b)

b[:7]=[0,0,0,0,0,0,0]#mengganti data 7 angka di awal
print(b)

b[4:-6]=[8,8,8,8,8]#menganti 5 angka di tengah
print(b)

b[3:-5]=[9,9,9,9,9,9,9]#menganti angka ke 9 sampai 16
print(b)