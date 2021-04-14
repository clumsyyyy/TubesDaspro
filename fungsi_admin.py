def verifyItem(ID, arr1, arr2):  # fungsi buat F05 buat verif
    isExisting = False
    ref_arr = []
    if ID[0] == "G":
        ref_arr = arr1
    elif ID[0] == "C":
        ref_arr = arr2
    for line in ref_arr:
        ref_id = line[0]
        if ref_id == ID:
            isExisting = True
    return isExisting

def tambahItem(arr1, arr2): #F05: MENAMBAH ITEM
    id_input = input("Masukkan ID: ")
    if (id_input[0] == "G" or id_input[0] == "C") and verifyItem(id_input, arr1, arr2) == False:
        new_name = input("Masukkan Nama: ")
        new_desc = input("Masukkan Deskripsi: ")
        new_jumlah = input("Masukkan Jumlah: ")
        new_rarity = input("Masukkan Rarity: ")
        if new_rarity == "C" or new_rarity == "B" or new_rarity == "A" or new_rarity == "S":
            if id_input[0] == "G":
                new_tahun = input("Masukkan Tahun Ditemukan: ")
                arr1.append([id_input, new_name, new_desc, new_jumlah, new_rarity, new_tahun])
                print("Item telah berhasil ditambahkan ke database\n")
            elif id_input[0] == "C":
                arr2.data_consumables.append([id_input, new_name, new_desc, new_jumlah, new_rarity])
                print("Item telah berhasil ditambahkan ke database.\n")
        else:
            print("Input Rarity tidak valid!\n")
    elif (id_input[0] == "G" or id_input[0] == "C") and verifyItem(id_input, arr1, arr2) == True:
        print("Gagal menambahkan item karena ID sudah ada.\n")
    else:
        print("Gagal menambahkan item karena ID tidak valid.\n")

def hapusItem(arr1, arr2):#F06: Hapus Item
    id_input = input("Masukkan ID: ")
    if id_input[0] == "G":
        ref_arr = arr1
    elif id_input[0] == "C":
        ref_arr = arr2
    item_index = 0
    i = -1
    if verifyItem(id_input, arr1, arr2) == True:
        for line in ref_arr:
            csv_arr = line
            i += 1
            if id_input == csv_arr[0]:
                item_index = i
                itemname = csv_arr[1]
        confirm = input("Apakah anda yakin ingin menghapus {} (Y/N)? ".format(itemname))
        if confirm == "Y":
            ref_arr.pop(item_index)
        elif confirm == "N":
            print("Penghapusan dibatalkan.")
    else:
        print("Tidak ada item dengan ID tersebut.")

def ubahJumlah(arr1, arr2):#F07: Ubah Jumlah
    id_input = input("Masukkan ID: ")
    if verifyItem(id_input, arr1, arr2) == True:
        quant = int(input("Masukkan jumlah: "))
        if id_input[0] == "G":
            ref_arr = arr1
        elif id_input[0] == "C":
            ref_arr = arr2
        for line in ref_arr:
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

