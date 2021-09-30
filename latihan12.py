while username == False:
    username = str(input('input username :'))
while password == False:
    password = str(input('input passwad  : '))
    password2 = str(input('input passwd2 : '))
    if username == "Bahry_semet":
        print('username benar')
    elif password == "admin":
        print('password benar')
        if password2 == "admin":
            print('password2 benar')
