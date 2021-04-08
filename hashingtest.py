def hashing2(str): #buat yang hashing, pake polynomial rolling function
    p = 56
    m = 1e9 + 9
    pangkat = 1
    val = 0

    for i in range(len(str)):
        val += (ord(str[i]) - ord('a') + 1) * (p ** pangkat)
        pangkat += 1
    return(int(val % m))

print(hashing2(input()))
