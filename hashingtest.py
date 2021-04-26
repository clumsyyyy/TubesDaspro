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


