def verifyItem(ID, arr1, arr2):  #fungsi verifikasi, dimodifikasi karena untuk fungsi admin di antara data gadget atau consumables
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


def tambahItem(arr1, arr2): #F05: Menambah Item
    id_input = input("Masukkan ID: ")

    if (id_input[0] == "G" or id_input[0] == "C") and verifyItem(id_input, arr1, arr2) == False: #jika awalan ID G atau C dan item belum ada sebelumnya

        new_name = input("Masukkan Nama: ")
        new_desc = input("Masukkan Deskripsi: ")
        new_jumlah = input("Masukkan Jumlah: ")
        new_rarity = input("Masukkan Rarity: ")

        while new_rarity != "C" and new_rarity != "B" and new_rarity != "A" and new_rarity != "S": #selama entry rarity tidak valid, minta masukan terus
            print("Input rarity tidak valid!")
            new_rarity = input("Masukkan Rarity: ")

        if new_rarity == "C" or new_rarity == "B" or new_rarity == "A" or new_rarity == "S": #jika rarity valid
            if id_input[0] == "G": #jika karakter awal ID == "G" (Gadget), minta input tahun

                new_tahun = input("Masukkan Tahun Ditemukan: ")
                arr1.append([id_input, new_name, new_desc, new_jumlah, new_rarity, new_tahun]) #tambahkan entry baru di array gadget
                print("Item telah berhasil ditambahkan ke database\n")

            elif id_input[0] == "C": #jika karakter awal ID == "C" (Consumables), tambahkan entry baru di array consumables
                arr2.append([id_input, new_name, new_desc, new_jumlah, new_rarity])
                print("Item telah berhasil ditambahkan ke database.\n")

    elif (id_input[0] == "G" or id_input[0] == "C") and verifyItem(id_input, arr1, arr2) == True: #jika item sudah ada sebelumnya, tidak akan dilakukan penambahan
        print("Gagal menambahkan item karena ID sudah ada.\n")
        tambahItem(arr1, arr2)

    elif (id_input == ""):
        print("Input kosong!")
        tambahItem(arr1, arr2)

    else: #jika input invalid
        print("Gagal menambahkan item karena ID tidak valid.\n")
        tambahItem(arr1, arr2)


def hapusItem(arr1, arr2):#F06: Hapus Item
    id_input = input("Masukkan ID: ")

    if id_input[0] == "G":
        ref_arr = arr1
    elif id_input[0] == "C":
        ref_arr = arr2

    item_index = 0
    i = -1

    if verifyItem(id_input, arr1, arr2) == True: #jika item ada
        for line in ref_arr:
            csv_arr = line
            i += 1 #penambahan i untuk ID
            if id_input == csv_arr[0]:
                item_index = i #mencocokkan indeks yang ingin dihapus dengan mencari ID di array referensi
                itemname = csv_arr[1]

        confirm = input("Apakah anda yakin ingin menghapus {} (Y/N)? ".format(itemname))

        if confirm == "Y": #jika dikonfirmasi, menggunakan fungsi pop, indeks akan dihapus
            ref_arr.pop(item_index)
            print("Item berhasil dihapus.")
        elif confirm == "N": #jika tidak jadi dihapus, maka prosedur akan berhenti
            print("Penghapusan dibatalkan.")

    elif (id_input == ""):
        print("Input kosong!")
        hapusItem(arr1, arr2)

    elif verifyItem(id_input, arr1, arr2) == False: #jika item tidak ada, output pesan error
        print("Tidak ada item dengan ID tersebut.")


def ubahJumlah(arr1, arr2):#F07: Ubah Jumlah
    id_input = input("Masukkan ID: ")

    if verifyItem(id_input, arr1, arr2) == True: #jika ID ada, mulai prosedur pengubahan
        quant = int(input("Masukkan jumlah: "))

        if id_input[0] == "G":
            ref_arr = arr1
        elif id_input[0] == "C":
            ref_arr = arr2

        for line in ref_arr:
            if line[0] == id_input:
                if int(line[3]) + quant > 0: #apabila jumlah pengubahan di atas 0 lakukan pengubahan
                    line[3] = str(int(line[3]) + quant)
                    if quant >= 0: #jika nilai pengubahan positif, maka outputnya "ditambahkan"
                        print("{} {} berhasil ditambahkan. Stok sekarang: {}".format(quant, line[1], line[3] ))
                    elif quant < 0: #jika nilai pengubahan negatif, outputnya "dibuang"
                        print("{} {} berhasil dibuang. Stok sekarang: {}".format(abs(quant), line[1], line[3] ))
                else: #jika pengubahan nanti bersifat negatif, maka jangan membuang
                    print("{} {} gagal dibuang karena stok kurang. Stok sekarang: {} (<{})".format(abs(quant), line[1], line[3], abs(quant)))

    else: #jika ID tidak ada, tidak perlu melakukan prosedur
        print("Tidak ada item dengan ID {}".format(id_input))


def helpAdmin() :
    print("========== HELP ==========")
    print("register - untuk melakukan registrasi user baru")
    print("login - untuk melakukan login ke dalam sistem")
    print("tambahitem - untuk melakukan penambahan item")
    print("hapusitem - untuk melakukan penghapusan suatu item pada database")
    print("ubahjumlah - untuk mengubah jumlah gadget dan consumable pada sistem")
    print("riwayatpinjam - untuk melihat riwayat peminjaman gadget")
    print("riwayatkembali - untuk melihat riwayat pengembalian gadget")
    print("riwayatambil - untuk melihat riwayat pengambilan consumable")


