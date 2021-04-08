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


def verifyItem(ID):  # fungsi buat F05 buat verif
    isExisting = False
    file = ""
    if ID[0] == "G":
        file = "gadget.csv"
    elif ID[0] == "C":
        file = "consumables.csv"
    with open(file, "r") as f:
        for line in f:
            csv_arr = splitter(line)
            ref_id = csv_arr[0]
            if ref_id == ID:
                isExisting = True
    if isExisting == True:
        return True
    else:
        return False


def printItem_Check(item_arr):
    print("Nama:", item_arr[1])
    print("Deskripsi:", item_arr[2])
    print("Jumlah: {} buah".format(item_arr[3]))
    print("Rarity:", item_arr[4])
    print("Tahun Ditemukan:", item_arr[5])
def cariRarity(): #F03: Pencarian Gadget Berdasarkan Rarity
    rarity = input("Masukkan rarity: ")
    print("\n")
    print("Hasil pencarian: ")
    with open("gadget.csv",  "r") as f:
        for line in f:
            csv_arr = splitter(line)
            item_rarity = csv_arr[4]
            id = csv_arr[0]
            if id[0] == "G":
                if rarity == item_rarity:
                    printItem_Check(csv_arr)

def cariTahun(): #F04: Pencarian Gadget Berdasarkan Tahun Ditemukan
    year = int(input("Masukkan tahun: "))
    category = input("Masukkan kategori: ")
    print("\n")
    print("Hasil pencarian: ")
    with open("gadget.csv", "r") as f:
        next(f)
        for line in f:
            csv_arr = splitter(line)
            item_year = int(csv_arr[5])
            id = csv_arr[0]
            if id[0] == "G":
                if category == ">" and item_year > year:
                    printItem_Check(csv_arr)
                if category == ">=" and item_year >= year:
                    printItem_Check(csv_arr)
                if category == "=" and item_year == year:
                    printItem_Check(csv_arr)
                if category == "<=" and item_year <= year:
                    printItem_Check(csv_arr)
                if category == "<" and item_year < year:
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
                new_gadget = id_input + ";" + new_name + ";" + new_desc + ";" + new_jumlah + ";" + new_rarity + ";" + new_tahun + "\n"
                with open("gadget.csv", "a") as f:
                    f.write(new_gadget)
                    f.close()
                print("Item telah berhasil ditambahkan ke database\n")
            elif id_input[0] == "C":
                new_consumable = id_input + ";" + new_name + ";" + new_desc + ";" + new_jumlah + ";" + new_rarity + "\n"
                with open("consumables.csv", "a") as f:
                    f.write(new_consumable)
                    f.close()
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
        file = "gadget.csv"
    elif id_input[0] == "C":
        file = "consumables.csv"
    itemname = ""
    if verifyItem(id_input) == True:
        with open(file, "r") as f:
            for line in f:
                csv_arr = splitter(line)
                if id_input == csv_arr[0]:
                    itemname = csv_arr[1]
        confirm = input("Apakah anda yakin ingin menghapus {} (Y/N)? ".format(itemname))
        if confirm == "Y":
            with open(file, "r") as f:
                lines = f.readlines()
            with open(file, "w") as f:
                for line in lines:
                    csv_arr = splitter(line)
                    if id_input != csv_arr[0]:
                        f.write(line)
        elif confirm == "N":
            print("Penghapusan dibatalkan.")
    else:
        print("Tidak ada item dengan ID tersebut.")

def ubahJumlah(): #F07 UBAH JUMLAH AAAAAAAAAAAAAAAAAAAAA
    id_input = input("Masukkan ID: ")
    item = []
    new_data = ""
    if id_input[0] == "G":
        file = "gadget.csv"
    elif id_input[0] == "C":
        file = "consumables.csv"
    if verifyItem(id_input) == True:
        quant = int(input("Masukkan jumlah: "))
        if id_input[0] == "G":
            with open("gadget.csv", "r") as f:
                for line in f:
                    csv_arr = splitter(line)
                    if id_input == csv_arr[0]:
                        item = csv_arr
                        if int(csv_arr[3]) + quant > 0:
                            item[3] = str(int(item[3]) + quant)
                            if quant < 0:
                                print("{} {} berhasil dibuang. Stok sekarang: {}".format(quant * -1, csv_arr[1], item[3]))
                                new_data = item[0] + ";" + item[1] + ";" + item[2] + ";" + str(int(item[3])) + ";" + item[4] + ";" + item[5]
                            elif quant > 0:
                                print("{} {} berhasil ditambahkan. Stok sekarang: {}".format(quant, csv_arr[1], item[3]))
                                new_data = item[0] + ";" + item[1] + ";" + item[2] + ";" + str(int(item[3])) + ";" + item[4] + ";" + item[5]
                        else:
                            print("{} {} gagal dibuang karena stok kurang. Stok sekarang: {} (<{})".format(quant * -1, item[1], item[3], quant * -1))
            f.close()
        elif id_input[0] == "C":
            with open("consumables.csv", "r") as f:
                for line in f:
                    csv_arr = splitter(line)
                    if id_input == csv_arr[0]:
                        item = csv_arr
                        if int(csv_arr[3]) + quant > 0:
                            item[3] = str(int(item[3]) + quant)
                            if quant < 0:
                                print("{} {} berhasil dibuang. Stok sekarang: {}".format(quant * -1, csv_arr[1], item[3]))
                                new_data = item[0] + ";" + item[1] + ";" + item[2] + ";" + str(int(item[3])) + ";" + item[4]
                            elif quant > 0:
                                print("{} {} berhasil ditambahkan. Stok sekarang: {}".format(quant, csv_arr[1], item[3]))
                                new_data = item[0] + ";" + item[1] + ";" + item[2] + ";" + str(int(item[3])) + ";" + item[4]
                        else:
                            print("{} {} gagal dibuang karena stok kurang. Stok sekarang: {} (<{})".format(quant * -1, item[1], item[3], quant * -1))
            f.close()

        with open(file, "r") as f:
            lines = f.readlines()
        with open(file, "w") as f:
            for line in lines:
                csv_arr = splitter(line)
                if id_input != csv_arr[0]:
                    f.write(line)
                elif id_input == csv_arr[0]:
                    f.write(new_data)
    else:
        print("Tidak ada item dengan ID tersebut!")