print("PROGRAM MENGHITUNG GAJI\n")
gaji=int(input("Input gaji pokok anda dalam sehari -> "))
gaji_bulan=gaji*22
#print("gaji pokok anda untuk satu bulan = Rp.",gaji_bulan)
print("=====================================================\n")

transport=int(input("Input transport anda dalam sehari -> "))
total_trans=transport*22
print("Total transport dalam sebulan \t\t= Rp.",total_trans)
print("=====================================================\n")

anak=input("Silahkan pilih jenis kelamin anak -> ")
if anak == "laki-laki" :
    Trans_anak = 15000
    TdanTA = total_trans + Trans_anak
elif anak == "perempuan":
    Trans_anak = 20000
    TdanTA = total_trans + Trans_anak
else:
    print("Jenis kelamin salah...!!!")

print("Transport untuk anak ",anak,"\t= Rp.",Trans_anak)
print("=====================================================\n")

print("Gaji pokok untuk satu bulan \t\t= Rp.",gaji_bulan)
print("Total transport + transport anak \t= Rp.", TdanTA)
totalgaji= TdanTA + gaji_bulan
print("Total gaji keseluruhan \t\t\t= Rp.", totalgaji)
print("=====================================================")
