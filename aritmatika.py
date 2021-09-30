def f():
    print("ini fungsi")
    print("selamat siang")

print (f())
def tambah(a=0, b=0):
    hasil = a + b
    return print("hasil tambah", hasil)

def mod(a=0, b=0):
    hasil = a % b
    return print("hasil mod", hasil)
def kali(a=0, b=0):
    hasil = a*b
    return print("hasil kali", hasil)
def kurang (a=0, b=0):
    hasil = a - b
    return print("hasil kurang", hasil)
def bagi(a=0, b=0):
    hasil = a / b
    return print("hasil bagi",hasil)



print(tambah(3,5))
print(mod(7,5))
print(kurang(4,3))
print(kali(4,4))
print(bagi(3,2))

