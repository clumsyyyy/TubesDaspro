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