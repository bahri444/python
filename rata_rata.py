p = input("massukkan Nilai praktikum: ")
uts = input("massukkan Nilai UAS: ")
uas = input("massukkan Nilai UTS :")
r = (int(p) + int(uts) + int(uas)) / 3

if r >= 90 and r <= 100 : grade = "A"
elif r >= 80 and r < 90 : grade = "B"
elif r >= 70 and r < 80 : grade = "C"
elif r >= 60 and r < 70 : grade = "D"
elif r >= 50 and r < 60 : grade = "E"
else :    grade = "anda tidak pernah mengikuti ujian"

print("nilai rata rata  : ", r)
print("dengan peringkat : ",grade)
