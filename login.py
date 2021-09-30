User = "admin"
Pass = "admin"
Pass2 = "admin"
replay = True
while replay:
    Username = str(input("input username :"))
    Passwd = str(input("input password  :"))
    Passwd2 = str(input("input password2 :"))

    if Username == User and (Passwd == Pass and Passwd2 == Pass2):
        print("login berhasil")
        print("wellcome to beranda !")
        replay = False
    else:
        print("login gagal")
        replay
