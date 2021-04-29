def verifyItem(ID, ref_arr):  # fungsi buat F05 buat verif
    isExisting = False
    for line in ref_arr:
        ref_id = line[0]
        if ref_id == ID:
            isExisting = True
    return isExisting

def printItem_Check(item_arr):
    print("Nama:", item_arr[1])
    print("Deskripsi:", item_arr[2])
    print("Jumlah: {} buah".format(item_arr[3]))
    print("Rarity:", item_arr[4])
    print("Tahun Ditemukan:", item_arr[5])
    print("\n")



def sortID(arr):
    for i in range(1, len(arr)):
        for j in range(1, len(arr) - i):
            if int(arr[j][0]) > int(arr[j + 1][0]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return(arr)


def cariRarity(arr): #F03: Pencarian Gadget Berdasarkan Rarity
    rarity = input("Masukkan rarity: ")
    print("\n")
    print("Hasil pencarian: ")
    for line in arr:
        csv_arr = line
        item_rarity = csv_arr[4]
        if rarity == item_rarity:
            printItem_Check(csv_arr)

def cariTahun(arr): #F04: Pencarian Gadget Berdasarkan Tahun Ditemukan
    year = int(input("Masukkan tahun: "))
    category = input("Masukkan kategori: ")
    print("\n")
    print("Hasil pencarian: ")
    for line in arr[1:]:
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


            
def pinjam(user_ID, borrow_array, ref_array): #F08 sama F10 ga jauh beda
    borrowed_id = input("Masukkan ID item: ")
    isBorrowed = False
    borrow_file_length = 0
    for line in borrow_array:
        borrow_file_length += 1
        if borrowed_id == line[2] and user_ID == line[1] and int(line[5]) == 0:
            isBorrowed = True
    
    if verifyItem(borrowed_id, ref_array) == True and isBorrowed == False:
        date = input("Tanggal peminjaman (DD/MM/YYYY): ") #anggap selalu valid
        quant = int(input("Jumlah peminjaman: "))

        for line in ref_array:
            if borrowed_id == line[0]:
                if int(line[3]) >= quant:
                    line[3] = str(int(line[3]) - quant)
                    print("Item {} (x{}) berhasil dipinjam!".format(line[1], quant))
                    borrow_array.append([str(borrow_file_length), user_ID, borrowed_id, date, str(quant), "0"])
                    sortID(borrow_array)
                elif int(line[3]) == 0:
                    print("Mohon maaf, barang sedang habis!")
                else:
                    print("Mohon maaf, jumlah peminjaman melebihi jumlah gadget yang ada!")
    elif verifyItem(borrowed_id, ref_array) == True and isBorrowed == True:
        print("Mohon maaf, Anda sedang meminjam item dengan ID yang sama!")
        pinjam(user_ID, borrow_array, ref_array)
    else:
        print("Tidak ada item dengan ID tersebut!")

def findName(id, arr):
    name = ""
    for line in arr:
        if id == line[0]:
            name = line[1]
    return name


personal_array = []
def kembalikan(user_ID, ref_array, borrow_array, return_array):
    global personal_array
    personal_array = [] #iuser id == 2, maka yang masuk cuman data peminjaman a.n. id nomor 2 (yang belum fully returned)
    i = 0
    #logikanya, baru diappend apabila data tidak ada di dalam data_return_gadget
    #setelah verifikasi dari user ID
    #cek pake boolean isReturned, kalo isReturned == False berarti baru di-append
    for line in borrow_array[1:]:
        isReturned = False
        isPartial = False
        if str(user_ID) == str(line[1]):
            if int(line[5]) == 1:
                isReturned = True
            elif int(line[5]) == 0:
                for return_line in return_array[1:]:
                    if int(return_line[3]) < int(line[4]) and line[0] == return_line[1]:
                        selisih = int(line[4]) - int(return_line[3]) 
                        isPartial = True

            if isPartial == True:
                i += 1
                personal_array.append([i, line[0], line[1], line[2], line[3], selisih])

            elif isReturned == False:
                i += 1
                personal_array.append([i, line[0], line[1], line[2], line[3], line[4]])
        
    #verifikasi apakah sesuai username
    if i != 0:
        for line in personal_array:
            print(str(line[0]) + ".", end = "")
            print(findName(line[3], ref_array), end = "")
            print(" (x{})".format(line[5]))
        ref_id = int(input("Masukkan nomor peminjaman: "))
        date = input("Tanggal pengembalian (DD/MM/YYYY): ")
        jumlah_pengembalian = int(input("Masukkan jumlah pengembalian: "))
        id_item = ""
        #belum buat validasi date (jadinya ga perlu)
        #if date valid:
        for line in personal_array:
            if ref_id == int(line[0]): #jika sesuai, berarti
                #tambahin data baru di data ngebalikin
                #return value, pake algoritma ubahJumlah ig
                quant = int(line[5])
                id_item = line[3]
                borrow_id = line[1]

        if quant == jumlah_pengembalian:
            for line in ref_array[1:]:
                if line[0] == id_item:
                    line[3] = str(int(line[3]) + quant)

            len_data = 1
            for line in return_array[1:]:
                len_data += 1
            return_array.append([str(len_data), borrow_id, date, quant])
            sortID(return_array)
            for line in borrow_array[1:]:
                if int(borrow_id) == int(line[0]):
                    line[5] = "1"

            print("\n")
            print("Item {} (x{}) telah dikembalikan.".format(findName(id_item, ref_array), quant))

        elif quant > jumlah_pengembalian:
            quant -= jumlah_pengembalian
            for line in ref_array[1:]:
                if line[0] == id_item:
                    line[3] = str(int(line[3]) + jumlah_pengembalian)

            len_data = 1

            for line in return_array[1:]:
                len_data += 1
            return_array.append([str(len_data), borrow_id, date, jumlah_pengembalian])
            sortID(return_array)

            print("\n")
            print("Item {} (x{}) telah dikembalikan. Sisa item: {}".format(findName(id_item, ref_array), jumlah_pengembalian, quant))
        elif quant < jumlah_pengembalian:
            print("Mohon maaf, tapi jumlah item yang dikembalikan lebih banyak dari yang dipinjam!")

    else:
        print("Mohon maaf, semua item nampaknya sudah dikembalikan atau Anda belum meminjam item!")

def minta(user_ID, borrow_array, ref_array):
    borrowed_id = input("Masukkan ID item: ")
    date = input("Tanggal permintaan (DD/MM/YYYY): ")
    quant = int(input("Jumlah permintaan: "))
    borrow_file_length = 0
    for line in borrow_array:
        borrow_file_length += 1
    if verifyItem(borrowed_id, ref_array) == True:
        for line in ref_array:
            if borrowed_id == line[0]:
                if int(line[3]) >= quant:
                    line[3] = str(int(line[3]) - quant)
                    print("Item {} (x{}) berhasil diambil!".format(line[1], quant))
                    borrow_array.append([str(borrow_file_length), user_ID, borrowed_id, date, str(quant)])
                    sortID(borrow_array)
                elif int(line[3]) == 0:
                    print("Mohon maaf, barang sedang habis!")
                else:
                    print("Mohon maaf, jumlah peminjaman melebihi jumlah gadget yang ada!")

    else:
        print("Tidak ada item dengan ID tersebut!")
