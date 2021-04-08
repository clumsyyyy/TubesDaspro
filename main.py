import fungsi_user as user
import fungsi_admin as admin
def splitter(string):  # gabole pake split jadi bikin sendiri h3h3
    split_value = [0 for i in range(100)]
    tmp = ''
    i = 0
    for word in string:
        if word == ';':
            split_value[i] = tmp
            i += 1
            tmp = ''
        else:
            tmp += word
    if tmp:
        split_value[i] = tmp
        i += 1
    return split_value

def login(): #F01: LOGIN
    user = input("Masukkan username: ")
    pw = input("Masukkan password: ")
    userFound = False
    isAdmin = False
    with open('user.csv', 'r') as f:
        for line in f:
            csv_arr = splitter(line)
            if user == csv_arr[2] and pw == csv_arr[3] and csv_arr[5] == "admin\n":
                userFound = True
                isAdmin = True
            elif user == csv_arr[2] and pw == csv_arr[3]:
                userFound = True
    if userFound == True and isAdmin == True:
        print("Halo {}! Selamat Datang di Kantong Ajaib.\n\n\n".format(user))
        main_admin()
    elif userFound == True and isAdmin == False:
        print("Halo {}! Selamat Datang di Kantong Ajaib.\n\n\n".format(user))
        main_user()
    else:
        print("Username/password tidak ditemukan! Silahkan masukkan lagi.")
        login()

def register(): #FO2: REGISTER
    new_name = input("Masukkan nama: ")
    new_user = input("Masukkan username: ")
    new_pw = input("Masukkan password: ")
    new_alamat = input("Masukkan alamat: ")
    doesNameExist = False
    count = 0
    with open("user.csv", "r") as f:
        for line in f:
            count += 1
            csv_acc = splitter(line)
            if csv_acc[2] == new_user:
                doesNameExist = True
    if doesNameExist == False:
        newcsv = str(count) + ";" + new_name + ";" + new_user + ";" + new_pw + ";" + new_alamat + ";user\n"
        with open("user.csv", "a") as f:
            f.write(newcsv)
            f.close()
        print("User {} berhasil diregistrasi.".format(new_user))
        loginmenu()
    else:
        print("Username tidak tersedia, mohon ganti username.")
        register()
    

def loginmenu():
    print("Selamat datang di Kantong Ajaib!")
    print("1. Register")
    print("2. Login")
    op = int(input(">>>"))
    if op == 1:
        register()
    elif op == 2:
        login()
    else:
        print("Opsi tidak sesuai")
        loginmenu()

        
def main_admin():
    print("\n[ADMIN CONTROL PANEL]\n")
    print("Ketik erintah: ")
    print("1. carirarity")
    print("2. caritahun")
    print("3. tambahitem")
    print("4. hapusitem")
    print("5. ubahjumlah")
    command = input(">>>")
    if command == "carirarity":
        admin.cariRarity()
    elif command == "caritahun":
        admin.cariTahun()
    elif command == "tambahitem":
        admin.tambahItem()
    elif command == "hapusitem":
        admin.hapusItem()
    elif command == "ubahjumlah":
        admin.ubahJumlah()
    main_admin()

def main_user():
    print("[CONTROL PANEL]\n")
    print("Ketik perintah: ")
    print("1. carirarity")
    print("2. caritahun")
    command = input(">>>")
    if command == "carirarity":
        user.cariRarity()
    elif command == "caritahun":
        user.cariTahun()
    main_user()


loginmenu() #MULAI DARI LOGINMENU
