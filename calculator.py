a = int(input("silahkan input angka pertama :"))
aritmatika = str(input("silahkan input operator [ +, -, *, / ]:"))
b = int(input("silahkan input angka kedua:"))

if aritmatika == '+':
    hasil = a+b
elif aritmatika == '-':
    hasil = a-b
elif aritmatika == '*':
    hasil = a*b
elif aritmatika == '/':
    hasil = a/b
print("hasil operasi aritmatika : ", a, aritmatika, b, " = ", hasil)
