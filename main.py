import time
import os
import hashingtest
import argparse
import datetime
import fungsi_user as user
import fungsi_admin as admin
parser = argparse.ArgumentParser(description = "testing argparse")
parser.add_argument('folder', type = str, help = 'Lokasi penyimpanan', default = '')
args = parser.parse_args()

def load():
    global data_user, data_gadget, data_consumables, data_borrow_gadget, data_borrow_consumables, data_return_gadget
    if os.path.exists(args.folder):
        with open(args.folder + "\\user.csv", "r") as f: #string = asu\n => string = asu
            data_user = [splitter(line.replace('\n', ''), ';') for line in f.readlines()] #.split()
        with open(args.folder + "\\gadget.csv", "r") as f:
            data_gadget = [splitter(line.replace('\n', ''), ';') for line in f.readlines()]
        with open(args.folder + "\\consumables.csv", "r") as f:
            data_consumables = [splitter(line.replace('\n', ''), ';') for line in f.readlines()]
        with open(args.folder + "\\gadget_borrow_history.csv", "r") as f:
            data_borrow_gadget = [splitter(line.replace('\n', ''), ';') for line in f.readlines()]
        with open(args.folder + "\\consumable_history.csv", "r") as f:
            data_borrow_consumables = [splitter(line.replace('\n', ''), ';') for line in f.readlines()]
        with open(args.folder + "\\gadget_return_history.csv", "r") as f:
            data_return_gadget = [splitter(line.replace('\n', ''), ';') for line in f.readlines()]
        print("Data berhasil di load!")
        clear()
    else:
        print("Folder load tidak ditemukan")
        data_user = [['id', 'username', 'nama', 'alamat', 'password', 'role']]
        data_gadget = [['id', 'nama', 'deskripsi', 'jumlah', 'rarity', 'tahun_ditemukan']]
        data_consumables = [['id', 'nama', 'deskripsi', 'jumlah', 'rarity']]
        data_borrow_gadget = [['id', 'id_peminjam', 'id_gadget', 'tanggal_peminjaman', 'jumlah', 'is_returned']]
        data_borrow_consumables = [['id', 'id_pengambil', 'id_consumable', 'tanggal_pengambilan', 'jumlah']]
        data_return_gadget = [['id', 'id_peminjaman', 'tanggal_pengembalian',]]
def save():
    global data_user, data_gadget, data_consumables, data_borrow_gadget, data_borrow_consumables, data_return_gadget
    folder = input("Masukkan nama folder penyimpanan: ")
    if not os.path.exists(folder):
        inp = input("Directory {} tidak ada, buat directory? ".format(folder))
        if inp == "Y" or inp == "y":
            os.makedirs(folder)
            args.folder = folder
        else:
            print("Save dibatalkan")
            return
    print()
    print("Saving....")
    with open(args.folder + "\\user.csv", "w+") as f:
        for line in data_user:
            for x in [line]:
                data = ";".join([str(a) for a in x])
                f.write(data)
                f.write("\n")
        #f.write('\n'.join([';'.join([str(a) for a in x]) for x in [line for line in data_user]]))
    with open(args.folder + "\\gadget.csv", "w+") as f:
        for line in data_gadget:
            for x in [line]:
                data = ";".join([str(a) for a in x])
                f.write(data + "\n")
    with open(args.folder + "\\consumables.csv", "w+") as f:
        for line in data_consumables:
            for x in [line]:
                data = ";".join([str(a) for a in x])
                f.write(data + "\n")
    with open(args.folder + "\\gadget_borrow_history.csv", "w+") as f:
        for line in data_borrow_gadget:
            for x in [line]:
                data = ";".join([str(a) for a in x])
                f.write(data + "\n")
    with open(args.folder + "\\consumable_history.csv", "w+") as f:
        for line in data_borrow_consumables:
            for x in [line]:
                data = ";".join([str(a) for a in x])
                f.write(data + "\n")
    with open(args.folder + "\\gadget_return_history.csv", "w+") as f:
        for line in data_return_gadget:
            for x in [line]:
                data = ";".join([str(a) for a in x])
                f.write(data + "\n")
    print("Data berhasil disimpan.")

def splitter(string, token):  # gabole pake split jadi bikin sendiri h3h3
    split_value = [] #a/b/c;d;e;f;g => splitter("a;b;c;d;e;f;g", "/") [a,b,c,d,e,f,g]
    tmp = ''
    for word in string:
        if word == token:
            split_value.append(tmp)
            tmp = ''
        else:
            tmp += word
    if tmp:
        split_value.append(tmp)
    return split_value

def clear():
    time.sleep(1)
    os.system('cls')
    
def clear_conf():
    input("[Tekan tombol manapun untuk kembali ke menu]")
    os.system('cls')
user_ID = ""

def login(): #F01: LOGIN
    global user_ID
    user = input("Masukkan username: ")
    pw = input("Masukkan password: ")
    hashedpw = hashingtest.hashing(pw)
    userFound = False
    isAdmin = False
    for line in data_user:
        csv_arr = line
        if user == csv_arr[2] and hashedpw == csv_arr[3] and csv_arr[5] == "admin":
            user_ID = csv_arr[0]
            userFound = True
            isAdmin = True
        elif user == csv_arr[2] and hashedpw == csv_arr[3]:
            user_ID = csv_arr[0]
            userFound = True
    if userFound == True and isAdmin == True:
        print("Halo {}! Selamat Datang di Kantong Ajaib.\n\n\n".format(user))
        clear()
        main_admin()
    elif userFound == True and isAdmin == False:
        print("Halo {}! Selamat Datang di Kantong Ajaib.\n\n\n".format(user))
        clear()
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
    for line in data_user:
        count += 1
        if line[2] == new_user:
            doesNameExist = True
    if doesNameExist == False:
        data_user.append([str(count), new_name, new_user, hashingtest.hashing(new_pw), new_alamat, "user"])
        print("User {} berhasil diregistrasi.".format(new_user))
        clear()
        main_admin()
    else:
        print("Username tidak tersedia, mohon ganti username.")
        clear()
        register()
def asciiart():
    print("_______________________________________________________________")
    print("|  _________________________________________________________  |")
    print("| | _  __         _                     _    _      _ _     | |")
    print("| || |/ /__ _ _ _| |_ ___ _ _  __ _    /_\  (_)__ _(_) |__  | |")
    print("| || ' </ _` | ' \  _/ _ \ ' \/ _` |  / _ \ | / _` | | '_ | | |")
    print("| ||_|\_\__,_|_||_\__\___/_||_\__, | /_/ \_\/ \__,_|_|_.__/ | |")
    print("| |                           |___/       |__/              | |")
    print("| |_________________________________________________________| |")
    print("|_____________________________________________________________|")
    print("\nSelamat datang di Kantong Ajaib!")
    print("================================")


def loginmenu():
    print("\nKetik perintah: ")
    print("[1] login")
    print("[2] help")
    print("[3] exit")
    command = input(">>> ")
    if command == "login":
        login()
    elif command == "help":
        admin.helpAdmin()
        loginmenu()
    elif command == "exit":
        print("Terima kasih telah menggunakan Kantong Ajaib!")
        time.sleep(3)
        exit()
    else:
        print("Perintah tidak dikenali! Mohon meng-input sesuai pilihan.")
        loginmenu()

def findUName(id, arr):
    name = ""
    for line in arr:
        if id == line[0]:
            name = line[2]
    return name

def main_admin():
    asciiart()
    global user_ID
    print("\n[ADMIN CONTROL PANEL]\n")
    print("Log-in sebagai: {}\n\n".format(findUName(user_ID, data_user)))
    print("Ketik perintah: ")
    print("[1] carirarity")
    print("[2] caritahun")
    print("[3] tambahitem")
    print("[4] hapusitem")
    print("[5] ubahjumlah")
    print("[6] register")
    print("[7] riwayatpinjam")
    print("[8] riwayatkembali")
    print("[9] riwayatambil")
    print("[10] save")
    print("[0] exit")
    command = input(">>> ")
    os.system('cls')
    print("Opsi: {}".format(command))
    print("\n")
    if command == "register":
        register()
    if command == "carirarity":
        user.cariRarity(data_gadget)
    elif command == "caritahun":
        user.cariTahun(data_gadget)
    elif command == "tambahitem":
        admin.tambahItem(data_gadget, data_consumables)
    elif command == "hapusitem":
        admin.hapusItem(data_gadget, data_consumables) #arr1 = data_Gadget, arr2 = data_consumables
    elif command == "ubahjumlah":
        admin.ubahJumlah(data_gadget, data_consumables)
    elif command == "save":
        save()
    elif command == "exit":
        save()
        exit()
    elif command == "riwayatpinjam":
        riwayatpinjam()
    elif command == "riwayatkembali":
        riwayatkembali()
    elif command == "riwayatambil":
        riwayatambil()
    clear_conf()
    main_admin()

def main_user():
    asciiart()
    global user_ID
    print("[Main Menu]\n")
    print("Log-in sebagai: {}\n\n".format(findUName(user_ID, data_user)))
    print("Ketik perintah: ")
    print("[1] carirarity")
    print("[2] caritahun")
    print("[3] pinjam")
    print("[4] kembalikan")
    print("[5] minta")
    print("[6] save")
    print("[7] exit")
    command = input(">>> ")
    os.system('cls')
    print("Opsi: {}".format(command))
    print("\n")
    if command == "carirarity":
        user.cariRarity(data_gadget)
    elif command == "caritahun":
        user.cariTahun(data_gadget)
    elif command == "save":
        save()
    elif command == "pinjam":
        user.pinjam(user_ID, data_borrow_gadget, data_gadget)
    elif command == "minta":
        user.minta(user_ID, data_borrow_consumables, data_consumables)
    elif command == "kembalikan":
        user.kembalikan(user_ID, data_gadget, data_borrow_gadget, data_return_gadget)
    elif command == "exit":
        save()
        exit()
    clear_conf()
    main_user()


def findName(id):
    name = ""
    for line in data_gadget:
        if id == line[0]:
            name = line[1]
    return name

def findConsum(id):
    name = ""
    for line in data_consumables:
        if id == line[0]:
            name = line[1]
    return name

        
def findUser(id):
    name = ""
    for line in data_user:
        if id == line[0]:
            name = line[1]
    return name

def riwayatpinjam():
    i = 0
    a = data_borrow_gadget[::-1]
    length = len(data_borrow_gadget) - 1
    for line in a[:length]:
        i += 1
        print("ID Peminjaman:", line[0] )
        print("Nama pengambil: ", end = "")
        print(findUser(line[1]))
        print("Nama gadget: ", end = "")
        print(findName(line[2]))
        print("Tanggal peminjaman:", line[3])
        print("Jumlah:", line[4])
        print("\n")
        if i % 5 == 0:
            inp = input("Tampilkan lebih banyak? (y/n)")
            if inp == "N" or inp == "n":
                main_admin()


def riwayatkembali():
    a = data_return_gadget[::-1]
    i = 0
    length = len(data_return_gadget) - 1
    
    for line in a[:length]:
        borrowed_item_id = ""
        for borrow_line in data_borrow_gadget[1:]:
            if int(line[1]) == int(borrow_line[0]):
                borrowed_item_id = borrow_line[2]
        i += 1
        print("ID Pengembalian: ", line[0])
        print("Nama pengambil: ", end = "")
        print(findUser(line[1]))
        print("Nama gadget: ", end = "")
        print(findName(borrowed_item_id))
        print("Tanggal peminjaman:", line[2])
        print("\n")
        if i % 5 == 0:
            inp = input("Tampilkan lebih banyak? (y/n)")
            if inp == "N" or inp == "n":
                main_admin()


def riwayatambil():
    i = 0
    a = data_borrow_consumables[::-1]
    length = len(data_borrow_consumables) - 1
    for line in a[:length]:
        i += 1
        print("ID Peminjaman:", line[0] )
        print("Nama pengambil: ", end = "")
        print(findUser(line[1]))
        print("Nama consumable: ", end = "")
        print(findConsum(line[2]))
        print("Tanggal pengambilan:", line[3])
        print("Jumlah:", line[4])
        print("\n")
        if i % 5 == 0:
            inp = input("Tampilkan lebih banyak? (y/n)")
            if inp == "N" or inp == "n":
                main_admin()
load()
asciiart()
loginmenu()