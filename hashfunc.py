def hashing(input):
    p = 56
    m = 1e9 + 9
    pangkat = 1
    val = 0

    for i in range(len(input)):
        val += (ord(input[i]) - ord('a') + 1) * (p ** pangkat)
        pangkat += 1
    hashed = str(int(val % m))
    return hashed

#fungsi hashing menggunakan algoritma polynomial rolling hash
#algoritma ini memanfaatkan perhitungan matematis dengan cara menjumlahkan nilai ASCII dari karakter
#yang dikalikan dengan konstanta p yang dipangkatkan dengan pangkat yang terus menerus meningkat sesuai indeks.
#untuk mencegah integer overflow, hasil akhir akan dimodulus dengan angka 1e9 + 9
#val adalah integer hasil akhir
