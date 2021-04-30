def verifyItem(ID, ref_arr):  #fungsi verifikasi keberadaan item
    isExisting = False
    for line in ref_arr:
        ref_id = line[0]
        if ref_id == ID:
            isExisting = True
    return isExisting


def printItem_Check(item_arr): #prosedur untuk mengeluarkan output sesuai format
    print("Nama:", item_arr[1])
    print("Deskripsi:", item_arr[2])
    print("Jumlah: {} buah".format(item_arr[3]))
    print("Rarity:", item_arr[4])
    print("Tahun Ditemukan:", item_arr[5])
    print("\n")


def sortID(arr): #fungsi mengurutkan array berdasarkan ID
    for i in range(1, len(arr)):
        for j in range(1, len(arr) - i):
            if int(arr[j][0]) > int(arr[j + 1][0]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return(arr)


def findName(id, arr): #fungsi untuk mencari nama (untuk F09)
    name = ""
    for line in arr:
        if id == line[0]:
            name = line[1]
    return name


def cariRarity(arr): #F03: Pencarian Gadget Berdasarkan Rarity
    rarity = input("Masukkan rarity: ")
    print("\n")
    print("Hasil pencarian: ")
    for line in arr:
        csv_arr = line
        item_rarity = csv_arr[4]
        if rarity == item_rarity: #jika rarity sesuai, lakukan print
            printItem_Check(csv_arr)


def cariTahun(arr): #F04: Pencarian Gadget Berdasarkan Tahun Ditemukan
    year = int(input("Masukkan tahun: "))
    category = input("Masukkan kategori: ")
    #input tahun dan kategori
    print("\n")
    print("Hasil pencarian: ")

    for line in arr[1:]:
        csv_arr = line
        item_year = int(csv_arr[5]) #pencocokan output sesuai kategori dan tahun
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


            
def pinjam(user_ID, borrow_array, ref_array): #F08: Pinjam Gadget
    borrowed_id = input("Masukkan ID item: ")
    isBorrowed = False #input ID

    borrow_file_length = 0

    for line in borrow_array:
        borrow_file_length += 1                                                     #penghitungan panjang file borrow
        if borrowed_id == line[2] and user_ID == line[1] and int(line[5]) == 0:     #jika barang ada di file peminjaman dan boolean flagnya "0"
            isBorrowed = True                                                       #barang tersebut sudah pernah dipinjam
    
    if verifyItem(borrowed_id, ref_array) == True and isBorrowed == False:
        date = input("Tanggal peminjaman (DD/MM/YYYY): ") #jika barang ada dan sedang tidak dipinjam lakukan prosedur peminjaman
        quant = int(input("Jumlah peminjaman: "))

        for line in ref_array:          #pengecekan traversal di array gadget
            if borrowed_id == line[0]:  #jika ID barang yang ingin dipinjam sesuai:

                if int(line[3]) >= quant: #jika jumlah stok lebih dari jumlah peminjaman
                    line[3] = str(int(line[3]) - quant) #kurangi jumla stok dengan jumlah peminjaman
                    print("Item {} (x{}) berhasil dipinjam!".format(line[1], quant)) #tambahkan entry baru dengan boolean flag 0
                    borrow_array.append([str(borrow_file_length), user_ID, borrowed_id, date, str(quant), "0"])
                    sortID(borrow_array)

                elif int(line[3]) == 0: #jika stok kosong
                    print("Mohon maaf, barang sedang habis!")

                else: 
                    print("Mohon maaf, jumlah peminjaman melebihi jumlah gadget yang ada!")

    elif verifyItem(borrowed_id, ref_array) == True and isBorrowed == True: #jika barang ada dan sedang dipinjam, maka tidak bisa dipinjam
        print("Mohon maaf, Anda sedang meminjam item dengan ID yang sama!") #fungsi dipanggil lagi
        pinjam(user_ID, borrow_array, ref_array)

    else: #jika ID tidak ada
        print("Tidak ada item dengan ID tersebut!")


personal_array = []
def kembalikan(user_ID, ref_array, borrow_array, return_array): #F09 + FB02: Pengembalian Gadget Penuh/Parsial
    global personal_array #personal array diibaratkan sebagai "inventory sementara" oleh user
    personal_array = [] #yang masuk hanya data peminjaman a.n. ID pengguna yang sedang login, jadi hanya item yang dipinjam a.n. ID pengguna
    #yang dapat dikembalikan (yang belum fully returned)
    i = 0
    #baru diappend apabila data tidak ada di dalam data_return_gadget
    #setelah verifikasi dari user ID
    #cek pake boolean isReturned, kalo isReturned == False berarti baru di-append
    for line in borrow_array[1:]:
        isReturned = False
        isPartial = False
        if str(user_ID) == str(line[1]):
            if int(line[5]) == 1:
                isReturned = True #jika boolean flag = "1", tidak perlu menambahkan peminjaman di personal_array
            elif int(line[5]) == 0:
                for return_line in return_array[1:]:
                    if int(return_line[3]) < int(line[4]) and line[0] == return_line[1]: #program mengecek apakah pengembalian yang dilakukan parsial atau tidak
                        selisih = int(line[4]) - int(return_line[3])                     #dengan mencocokkan ID yang ada dan menghitung selisih yang perlu dikembalikan
                        isPartial = True   

            if isPartial == True: #jika pengembalian parsial, maka tambahkan entry di personal_array dengan jumlah yang perlu dikembalikan = selisih
                i += 1
                personal_array.append([i, line[0], line[1], line[2], line[3], selisih])

            elif isReturned == False: #jika belum dikembalikan sama sekali, maka tambahkan entry di personal_array sesuai dengan borrow_array
                i += 1
                personal_array.append([i, line[0], line[1], line[2], line[3], line[4]])
        

    if i != 0: #jika personal_array tidak kosong
        for line in personal_array:
            print(str(line[0]) + ".", end = "") #output formatting untuk pengembalian
            print(findName(line[3], ref_array), end = "")
            print(" (x{})".format(line[5]))

        
        ref_id = int(input("Masukkan nomor peminjaman: "))
        date = input("Tanggal pengembalian (DD/MM/YYYY): ")
        jumlah_pengembalian = int(input("Masukkan jumlah pengembalian: "))
        id_item = ""
        #tidak perlu validasi tanggal karena tanggal diasumsikan sudah valid dari masukan (sesuai spesifikasi)
        #if date valid:
        for line in personal_array:
            if ref_id == int(line[0]): #jika sesuai, berarti
                #ambil data sesuai entry yang diinginkan
                quant = int(line[5])
                id_item = line[3]
                borrow_id = line[1]

        if quant == jumlah_pengembalian: #kasus pengembalian penuh
            #tambahkan jumlah pengembalian ke borrow_array di entry ID item yang sesuai
            for line in ref_array[1:]:
                if line[0] == id_item:
                    line[3] = str(int(line[3]) + quant)

            len_data = 1 #len_data digunakan untuk penambahan ID di entry

            for line in return_array[1:]:
                len_data += 1
            return_array.append([str(len_data), borrow_id, date, quant])
            sortID(return_array)
            #sort array berdasarkan ID agar lebih rapi

            for line in borrow_array[1:]:
                if int(borrow_id) == int(line[0]):
                    line[5] = "1"
            #ubah boolean flag menjadi 1 (pengembalian lunas)

            print("\n")
            print("Item {} (x{}) telah dikembalikan.".format(findName(id_item, ref_array), quant))

        elif quant > jumlah_pengembalian: #kasus pengembalian parsial
            quant -= jumlah_pengembalian
            for line in ref_array[1:]:
                if line[0] == id_item:
                    line[3] = str(int(line[3]) + jumlah_pengembalian)
                #tambahkan jumlah pengembalian ke borrow_array di entry ID item yang sesuai

            len_data = 1

            for line in return_array[1:]:
                len_data += 1
            return_array.append([str(len_data), borrow_id, date, jumlah_pengembalian])
            sortID(return_array)

            #boolean flag tetap 0, berarti item masih dapat dikembalikan nantinya

            print("\n")
            print("Item {} (x{}) telah dikembalikan. Sisa item: {}".format(findName(id_item, ref_array), jumlah_pengembalian, quant))

        elif quant < jumlah_pengembalian: #kasus jumlah pengembalian lebih besar dari peminjaman
            print("Mohon maaf, tapi jumlah item yang dikembalikan lebih banyak dari yang dipinjam!")

    else: #jika personal_array kosong
        print("Mohon maaf, semua item nampaknya sudah dikembalikan atau Anda belum meminjam item!")



def minta(user_ID, borrow_array, ref_array): #F10: Meminta Item
    borrowed_id = input("Masukkan ID item: ") #input nama item, tanggal, dan kuantitas
    date = input("Tanggal permintaan (DD/MM/YYYY): ")
    quant = int(input("Jumlah permintaan: "))

    borrow_file_length = 0
    for line in borrow_array:
        borrow_file_length += 1

    if verifyItem(borrowed_id, ref_array) == True:      #jika ID item ada, akan dilakukan pengecekan traversal
        for line in ref_array:
            if borrowed_id == line[0]:
                if int(line[3]) >= quant:               #jika jumlah item lebih banyak dari kuantitas, peminjaman dilakukan, jumlah di array consumables dikurangi
                    line[3] = str(int(line[3]) - quant)
                    print("Item {} (x{}) berhasil diambil!".format(line[1], quant))
                    borrow_array.append([str(borrow_file_length), user_ID, borrowed_id, date, str(quant)]) #penambahan entry baru di borrow_array
                    sortID(borrow_array)

                elif int(line[3]) == 0: #jika item == 0, maka muncul pesan bahwa barang sedang habis
                    print("Mohon maaf, barang sedang habis!")

                else: #jika jumlah permintaan lebih besar dari stok
                    print("Mohon maaf, jumlah peminjaman melebihi jumlah consumable yang ada!")

    else: #jika tidak ditemukan item
        print("Tidak ada item dengan ID tersebut!")
