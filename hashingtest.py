def hashing(str):


    p = 56
    m = 1e9 + 9
    pangkat = 1
    val = 0

    for i in range(len(str)):
        val = (val + (ord(str[i]) - ord('a') + 1) * pangkat) % m
        pangkat *= p % m
    return int(val)

def hashing2(str):
    p = 56
    m = 1e9 + 9
    pangkat = 1
    val = 0

    for i in range(len(str)):
        val += (ord(str[i]) - ord('a') + 1) * (p ** pangkat)
        pangkat += 1
    return(int(val % m))

print(hashing2(input()))

for i in range(95, -1, -1):
     print("{} shell".format(i))