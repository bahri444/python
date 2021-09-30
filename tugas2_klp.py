def que():#deklaraasi fungsi que
    s=[]
    return s
def enque(s,i):#deklaraasi fungsi enque
    s.insert(0,i)
    return s
def deque(s):#deklaraasi fungsi deque
    return s.pop()
def rear(s):#deklaraasi fungsi year
    return (s[0])
def front(s):#deklaraasi fungsi front
    return (s[len(s)-1])
def size(s):#deklaraasi fungsi size
    return len(s)
def isEmpty(s):#deklaraasi fungsi is empty
    return s==[]
def no2():#deklaraasi fungsi no2
    s=que()
    Tanya=''#deklaraasi variabel tanya dengan value caharacter
    while True:#deklaraasi looping dengan kondisi true
        banyak=int(input('masukkan banyak orang yang ingin bermain :'))#variabel banyak di gunakan untuk menginput data jumlah orang yang akan bermain, dengan tipe data integer
        for i in range (banyak):#looping for di gunakan untuk mengulagi nilai yang di inputkan di variabel banyak
            orang=input('input nama orang ke-%i yang masuk di antrian :'%i)#variabelhttps://youtu.be/ktRK_8p9L34 orang di gunakan untuk menginput data jumlah orang yang berada di antrian, menggunakan data tipe string 
            enque(s,orang)#fungsi enque dengan atribut s,orang u ntuk menampung data yang di inputkan di variabel orang
        s.reverse()#
        print('nama-nama orang yang berada di antrian %s' %s)#menampilkan nama orang yang sudah terdaftar di antrian
        s.reverse()#
        search=input('silahkan cari nama orang yang bermain ! :')#variabel search di gunakan untuk mencari data melalui inputan oleh useer yang ingin mencari data nama pemain menggunkan string
        ditemukan='t'#variabel ditemukan dengan value t(tidak)
        hitung=0#variabel hitung di gunakan untuk memulai hitungan dari angka nol(0)
        while ditemukan=='t':#looping isi variabel ditemukan
            if search==front(s):#jika nailai variabel search sama dengan fungsi front dengan atribut s maka orang yang di cari di teukan
                print('orang yang anda cari di temukan')
                ditemukan='y'
            elif search!=front(s):#jika variabel search tidak sama dengan fungsi front dengan atribut s maka orang yang di cari tidak di temukan
                masukan=deque(s)#variabel masukan di guunakan untuk menggabungkan value string yang di inputkan oleh user dari velue ke-1 sampai value ke n
                enque(s,masukan)
                ditemukan='t'
                s.reverse()
                print('loop %i=%s'%((hitung+1),s))#menampilkan semua data yang telah di inputkan oleh user
                s.reverse()
            hitung+=1#untuk melooping value sesuai yang di inputkan user
            if hitung >len(s):#jika hitung lebih besar daripada elemen class s maka orang yang di cari tidak ada
                print('orang yang di cari tidak ada')
                ditemukan='y'
        print('total lopping yang di perlukan adalah',str(hitung-1))#output jumlah loping yang di lakukan di variabel hitung
        Tanya=input('Apakah anda ingin melanjutkan permainan Y/N ?')#variabel tanya di gunakan untuk menerima inputan value dari user berupa string
        if Tanya=='Y':#jika value variabel tanya sama dengan Y maka permainan akan di lanjutkan
            print("OKEH MARI KITA LANJUTKAN!")
        elif Tanya=='N':#jika value dari variabel tanya sama dengan N maka permainan akan di hentikan
            print('===================================================')
            print('=====================Finish========================')
            break #mengembalikan value nol(0) agar permainan di hentikan
no2()#akhir dari blok fungsi no2 (penutup program)


