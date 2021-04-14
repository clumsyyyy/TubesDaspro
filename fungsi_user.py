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

def printItem_Check(item_arr):
    print("Nama:", item_arr[1])
    print("Deskripsi:", item_arr[2])
    print("Jumlah: {} buah".format(item_arr[3]))
    print("Rarity:", item_arr[4])
    print("Tahun Ditemukan:", item_arr[5])
    print("\n")

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
    date = input("Tanggal peminjaman: ")
    quant = int(input("Jumlah peminjaman: "))
    borrow_file_length = 0
    for line in borrow_array:
        borrow_file_length += 1
    if verifyItem(borrowed_id, ref_array, borrow_array) == True:
        for line in ref_array:
            if borrowed_id == line[0]:
                if int(line[3]) > quant:
                    line[3] = str(int(line[3]) - quant)
                    print("Item {} (x{}) berhasil dipinjam!".format(line[1], quant))
                    borrow_array.append([str(borrow_file_length), user_ID, borrowed_id, date, str(quant)])
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
    print("\n")
    global personal_array
    i = 0
    for line in borrow_array[1:]:
        if str(user_ID) == str(line[1]):
            i += 1
            line[0] = i
            personal_array.append(line)
    print(personal_array)
    for line in personal_array:
        print(str(line[0]) + ".", end = "")
        print(findName(line[2], ref_array))
    ref_id = int(input("Masukkan nomor peminjaman: "))
    date = input("Tanggal pengembalian: ")
    id_item = ""
    #belum buat validasi date (jadinya ga perlu)
    #if date valid:
    for line in personal_array:
        if ref_id == int(line[0]): #jika sesuai, berarti
             #tambahin data baru di data ngebalikin
             #return value, pake algoritma ubahJumlah ig
            quant = int(line[4])
            id_item = line[2]
    for line in ref_array[1:]:
        if line[0] == id_item:
            line[3] = str(int(line[3]) + quant)
    len_data = 1
    for line in return_array[1:]:
        len_data += 1
    return_array.append([str(len_data), user_ID, id_item, date])

def minta(user_ID, borrow_array, ref_array):
    borrowed_id = input("Masukkan ID item: ")
    date = input("Tanggal peminjaman: ")
    quant = int(input("Jumlah peminjaman: "))
    borrow_file_length = 0
    for line in borrow_array:
        borrow_file_length += 1
    if verifyItem(borrowed_id, borrow_array, ref_array) == True:
        for line in ref_array:
            if borrowed_id == line[0]:
                if int(line[3]) > quant:
                    line[3] = str(int(line[3]) - quant)
                    print("Item {} (x{}) berhasil diambil!".format(line[1], quant))
                    borrow_array.append([str(borrow_file_length), user_ID, borrowed_id, date, str(quant)])
    else:
        print("Tidak ada item dengan ID tersebut!")