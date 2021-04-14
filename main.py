import time
import os
import hashingtest
import argparse
import datetime
parser = argparse.ArgumentParser(description = "testing argparse")
parser.add_argument('folder', type = str, help = 'Lokasi penyimpanan', default = '')
args = parser.parse_args()

def splitter(string, token):  # gabole pake split jadi bikin sendiri h3h3
    split_value = [0 for i in range(6)]
    tmp = ''
    i = 0
    for word in string:
        if word == token:
            split_value[i] = tmp
            i += 1
            tmp = ''
        else:
            tmp += word
    if tmp:
        split_value[i] = tmp
        i += 1
    return split_value

def clear():
    time.sleep(1)
    os.system('cls')
    
def clear_conf():
    input("Tekan tombol manapun untuk kembali ke menu....")
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
    

def loginmenu():
    print("Selamat datang di Kantong Ajaib!")
    login()

        
def main_admin():
    print("\n[ADMIN CONTROL PANEL]\n")
    print("Ketik perintah: ")
    print("carirarity")
    print("caritahun")
    print("tambahitem")
    print("hapusitem")
    print("ubahjumlah")
    print("save")
    print("exit")
    print("register")
    print("riwayatpinjam")
    print("riwayatambil")
    command = input(">>> ")
    os.system('cls')
    if command == "register":
        register()
    if command == "carirarity":
        cariRarity()
    elif command == "caritahun":
        cariTahun()
    elif command == "tambahitem":
        tambahItem()
    elif command == "hapusitem":
        hapusItem()
    elif command == "ubahjumlah":
        ubahJumlah()
    elif command == "save":
        save()
    elif command == "exit":
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
    global user_ID
    print("[CONTROL PANEL]\n")
    print("user id: {}".format(user_ID))
    print("Ketik perintah: ")
    print("1. carirarity")
    print("2. caritahun")
    print("3. pinjam")
    print("4. minta")
    print("5. save")
    print("6. kembalikan")
    print("7. exit")
    command = input(">>> ")
    if command == "carirarity":
        cariRarity()
    elif command == "caritahun":
        cariTahun()
    elif command == "save":
        save()
    elif command == "pinjam":
        pinjam(user_ID)
    elif command == "minta":
        minta(user_ID)
    elif command == "kembalikan":
        kembalikan(user_ID)
    elif command == "exit":
        exit()
    main_user()


def load():
    global data_user, data_gadget, data_consumables, data_borrow_gadget, data_borrow_consumables, data_return_gadget
    if os.path.exists(args.folder):
        with open(args.folder + "\\user.csv", "r") as f:
            data_user = [splitter(line.replace('\n', ''), ';') for line in f.readlines()]
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
        data_borrow_gadget = [['id', 'id_peminjam', 'id_gadget', 'tanggal_peminjaman', 'jumlah']]
        data_borrow_consumables = [['id', 'id_pengambil', 'id_consumable', 'tanggal_peminjaman']]
        data_return_gadget = [['id', 'id_peminjam', 'id_gadget', 'tanggal_peminjaman', 'jumlah']]

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
    clear()

def verifyItem(ID):  # fungsi buat F05 buat verif
    isExisting = False
    file = ""
    if ID[0] == "G":
        file = data_gadget
    elif ID[0] == "C":
        file = data_consumables
    for line in file:
        csv_arr = line
        ref_id = csv_arr[0]
        if ref_id == ID:
            isExisting = True
    return isExisting

def printItem_Check(item_arr):
    print("Nama:", item_arr[1])
    print("Deskripsi:", item_arr[2])
    print("Jumlah: {} buah".format(item_arr[3]))
    print("Rarity:", item_arr[4])
    print("Tahun Ditemukan:", item_arr[5])

def cariTahun(): #F04: Pencarian Gadget Berdasarkan Tahun Ditemukan
    year = int(input("Masukkan tahun: "))
    category = input("Masukkan kategori: ")
    print("\n")
    print("Hasil pencarian: ")
    for line in data_gadget[1:]:
        csv_arr = line
        item_year = int(csv_arr[5])
        if category == ">" and item_year > year:
            printItem_Check(csv_arr)
        elif category == ">=" and item_year >= year:
            printItem_Check(csv_arr)
        elif category == "=" and item_year == year:
            printItem_Check(csv_arr)
        elif category == "<=" and item_year <= year:
            printItem_Check(csv_arr)
        elif category == "<" and item_year < year:
            printItem_Check(csv_arr)

def cariRarity(): #F03: Pencarian Gadget Berdasarkan Rarity
    rarity = input("Masukkan rarity: ")
    print("\n")
    print("Hasil pencarian: ")
    for line in data_gadget:
        csv_arr = line
        item_rarity = csv_arr[4]
        if rarity == item_rarity:
            printItem_Check(csv_arr)

def tambahItem(): #F05: MENAMBAH ITEM
    id_input = input("Masukkan ID: ")
    if (id_input[0] == "G" or id_input[0] == "C") and verifyItem(id_input) == False:
        new_name = input("Masukkan Nama: ")
        new_desc = input("Masukkan Deskripsi: ")
        new_jumlah = input("Masukkan Jumlah: ")
        new_rarity = input("Masukkan Rarity: ")
        if new_rarity == "C" or new_rarity == "B" or new_rarity == "A" or new_rarity == "S":
            if id_input[0] == "G":
                new_tahun = input("Masukkan Tahun Ditemukan: ")
                data_gadget.append([id_input, new_name, new_desc, new_jumlah, new_rarity, new_tahun])
                print("Item telah berhasil ditambahkan ke database\n")
            elif id_input[0] == "C":
                data_consumables.append([id_input, new_name, new_desc, new_jumlah, new_rarity])
                print("Item telah berhasil ditambahkan ke database.\n")
        else:
            print("Input Rarity tidak valid!\n")
    elif (id_input[0] == "G" or id_input[0] == "C") and verifyItem(id_input) == True:
        print("Gagal menambahkan item karena ID sudah ada.\n")
    else:
        print("Gagal menambahkan item karena ID tidak valid.\n")

def hapusItem():#F06: Hapus Item
    id_input = input("Masukkan ID: ")
    if id_input[0] == "G":
        file = data_gadget
    elif id_input[0] == "C":
        file = data_consumables
    item_index = 0
    i = -1
    if verifyItem(id_input) == True:
        for line in file:
            csv_arr = line
            i += 1
            if id_input == csv_arr[0]:
                item_index = i
                itemname = csv_arr[1]
        confirm = input("Apakah anda yakin ingin menghapus {} (Y/N)? ".format(itemname))
        if confirm == "Y":
            data_gadget.pop(item_index)
        elif confirm == "N":
            print("Penghapusan dibatalkan.")
    else:
        print("Tidak ada item dengan ID tersebut.")


def ubahJumlah():#F07: Ubah Jumlah
    id_input = input("Masukkan ID: ")
    if verifyItem(id_input) == True:
        quant = int(input("Masukkan jumlah: "))
        if id_input[0] == "G":
            file = data_gadget
        elif id_input[0] == "C":
            file = data_consumables
        for line in file:
            if line[0] == id_input:
                if int(line[3]) + quant > 0:
                    line[3] = str(int(line[3]) + quant)
                    if quant >= 0:
                        print("{} {} berhasil ditambahkan. Stok sekarang: {}".format(quant, line[1], line[3] ))
                    elif quant < 0:
                        print("{} {} berhasil dibuang. Stok sekarang: {}".format(abs(quant), line[1], line[3] ))
                else:
                    print("{} {} gagal dibuang karena stok kurang. Stok sekarang: {} (<{})".format(abs(quant), line[1], line[3], abs(quant)))
    else:
        print("Tidak ada item dengan ID {}".format(id_input))


    
def pinjam(user_ID): #F08 sama F10 ga jauh beda
    borrowed_id = input("Masukkan ID item: ")
    date = input("Tanggal peminjaman: ")
    quant = int(input("Jumlah peminjaman: "))
    borrow_file_length = 0
    for line in data_borrow_gadget:
        borrow_file_length += 1
    if verifyItem(borrowed_id) == True:
        for line in data_gadget:
            if borrowed_id == line[0]:
                if int(line[3]) > quant:
                    line[3] = str(int(line[3]) - quant)
                    print("Item {} (x{}) berhasil dipinjam!".format(line[1], quant))
                    data_borrow_gadget.append([str(borrow_file_length), user_ID, borrowed_id, date, str(quant)])
    else:
        print("Tidak ada item dengan ID tersebut!")

def minta(user_ID):
    borrowed_id = input("Masukkan ID item: ")
    date = input("Tanggal peminjaman: ")
    quant = int(input("Jumlah peminjaman: "))
    borrow_file_length = 0
    for line in data_borrow_consumables:
        borrow_file_length += 1
    if verifyItem(borrowed_id) == True:
        for line in data_consumables:
            if borrowed_id == line[0]:
                if int(line[3]) > quant:
                    line[3] = str(int(line[3]) - quant)
                    print("Item {} (x{}) berhasil diambil!".format(line[1], quant))
                    data_borrow_consumables.append([str(borrow_file_length), user_ID, borrowed_id, date, str(quant)])
    else:
        print("Tidak ada item dengan ID tersebut!")

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


personal_array = []

def kembalikan(user_ID):
    print("\n")
    global personal_array
    i = 0
    for line in data_borrow_gadget[1:]:
        if str(user_ID) == str(line[1]):
            i += 1
            line[0] = i
            personal_array.append(line)
    print(personal_array)
    for line in personal_array:
        print(str(line[0]) + ".", end = "")
        print(findName(line[2]))
    ref_id = int(input("Masukkan nomor peminjaman: "))
    date = input("Tanggal pengembalian: ")
    id_item = ""
    #belum buat validasi date
    #if date valid:
    for line in personal_array:
        if ref_id == int(line[0]): #jika sesuai, berarti
             #tambahin data baru di data ngebalikin
             #return value, pake algoritma ubahJumlah ig
            quant = int(line[4])
            id_item = line[2]
            print(id_item)
    for line in data_gadget[1:]:
        if line[0] == id_item:
            line[3] = str(int(line[3]) + quant)
            print(line[3])
    len_data = 1
    for line in data_return_gadget[1:]:
        len_data += 1
    data_return_gadget.append([str(len_data), user_ID, id_item, date])
    print(data_return_gadget)

        
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
        i += 1
        print("ID Pengembalian: ", line[0])
        print("Nama pengambil: ", end = "")
        print(findUser(line[1]))
        print("Nama gadget: ", end = "")
        print(findName(line[2]))
        print("Tanggal peminjaman:", line[3])
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
loginmenu()