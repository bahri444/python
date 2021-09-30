hari = ["Senin","Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu", "Minggu"]
print("Nama : Saepul Bahri")
for i in range(len(hari)):
    print(i + 1,hari[i])
    if i== 4: 
        print("     Hari masuk kuliah")
    elif i == 6:
        print("     Hari libur kuliah")
