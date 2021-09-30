from datetime import timedelta, datetime#deklarasi package untuk mempungsikan atribut date time
from time import sleep

class Queue:#deklarasi class queitrhttpsem
	def __init__(self):#deklarasi fungsi init
		self.item = []
	def isEmpty(self):#deklarasi fungsi isempty
		return self.item == []
	def enqueue(self,item):#deklarasi fungsi enque
		self.item.insert(0,item)
	def dequeue(self):#deklarasi fungsi deque
		return self.item.pop()
	def rear(self):#deklarasi fungsi rear
		return self.items[0]
	def front(self):#deklarasi fungsi front
		return self.items[len(self.items) - 1 ]
	def size(self):#deklarasi fungsi size
		return len(self.item)
	def open(self):#deklarasi fungsi openclass que
		return self.item

def antrian():#awal deklarasi fungsi antrian
	endtime = datetime.now() + timedelta(seconds = 2)#variabel endtime untuk membanggunakan waktu sekarang dengan beda eksekusi 2 detik pada milisecond-nya
	tanda = 'n'#deklarasi variabel tanda dengan value 'n'
	m = Queue()#deklarasi variabel m dengan class queue
	cad = Queue()#deklarasi variabel cad dengan class queue
	inputan = int(input('masukkan berapa orang yang ingin antri = '))#variabel input untuk menerima inputan jumlah dari user berupa intger
	for i in range(inputan):#untuk mengeksekusi value dan me-loopingnya sesuai dengan jumlah intger yang di inputkan oleh user
		nama = input('masukkan nama customer ke %i = '%(i + 1))#variabel nama untuk menerima inputan data nama dengan value string dengan '%i = '%(i + 1))melooping nomor hingga terus bertambah satu sampai batas yang di inputkan user
		m.enqueue(nama)#menyimpan sementara value dari variabel nama
		cad.enqueue(nama)#menyimpan sementara value dari variabel nama dan nomor antrian dari variabel card1
		
	print("estimasi jam pelayanan costumer")#menampilakan kata "estimasi jam pelayanan customer" ke layar
	while not m.isEmpty():#looping method m.isempty yang tidak kosong
		if not m.isEmpty():#jika method isempty tidak kosong
			if tanda == 'n':#jika value dari variabel tandaitrhttpsem sama dengan value 'n' maka eksekusi code di dalam blok if akan di jalankan
				print(m.dequeue(),'akan dilayani pada : ',datetime.now())#menentukan waktu pelayanan sesuai waktu(sekarang) saat eksekusi program di jalankan oleh user untuk nama orang yang sudah terdaftar sesuai urutan
				tanda = 'y'
			else:
				print(m.dequeue(),'akan dilayani pada :' ,endtime)
				endtime = endtime + timedelta(seconds = 2)#membuat output waktu antrian yang satu dengan yang lain menjadi berbeda 2 detik
	
	tanda = 'n'#jika variabel tanda sama dengan value 'n' maka eksekusi kode di bawahnya akan di lanjutkan
	print("======================antrian======================")
	while not cad.isEmpty():
		if not cad.isEmpty():
			if tanda == 0:
				print(cad.dequeue(),'sedang dilayani')#method card.deque menampilkan nama orang yang sedang di layani sesuai dengan nomor antrian kartu(cad)
				tanda=1
			else:
				sleep(2)#untuk menghentikan program sejenak(2 detik). sehingga statement dibawahnya tidak akan dieksekusi sampai pemberhentian waktu selesai.
				print(cad.dequeue(),'sedang dilayani')#method cad.deque menampilkan nama orang yang sedang di layani sesuai dengan nomor kartu(cad)
	if cad.isEmpty():#jika variabel cad.isempty sudah kosong maka akan menampilkan ===antrian telah habis===
		print("===============antrian telah habis==============")		
antrian()#akhir dari fungsi antrian