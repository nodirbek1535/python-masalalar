son = 12345
teskari_son = int(str(son)[::-1])
print(teskari_son)










def maxsus_elementlar_soni(mat):
    n = len(mat)
    m = len(mat[0])
    soni = 0

    for i in range(n):
        for j in range(m):
            ustun_yigindi = sum(mat[x][j] for x in range(n))

            chapdagilar = mat[i][:j]
            ongdagilar = mat[i][j+1:]

            # Shartlarni tekshiramiz
            if (mat[i][j] > ustun_yigindi and
                all(mat[i][j] > x for x in chapdagilar) and
                all(mat[i][j] < x for x in ongdagilar)):
                soni += 1

    return soni

# Misol uchun matritsa
matritsa = [
    [2, 5, 3],
    [1, 8, 6],
    [4, 7, 9]
]

print("Maxsus elementlar soni:", maxsus_elementlar_soni(matritsa))


matrisa = [
    [1,2,3,4,5,6,7,8,9,10,11,12],
    [45,23,5,3,5,3,5,3,32,2,4,2],
    [1,23,45,56,22,12,354,3,23,3,53,3],
    [9,8,7,6,5,4,4,3,2,1,1,12],
    [9,8,7,654,23,3,45,2,13,56,5,53],
    [33,44,53,2,1,3,354,6,6,7,5,443],
    [12,3,4,4,5,5,66,6,1,76,7,7],
    [334,3,43,2,2,4,45,55,6,6,5,4]
]

n = 8
m = 12

def ustun_yigindi(mat, satr, ustun):
    summa = 0
    for i in range(n):
        if i != satr:
            summa += mat[i][ustun]
    return summa

def chap_tekshirish(mat, satr, ustun):
    for j in range(ustun):
        if mat[satr][j] >= mat[satr][ustun]:
            return False
    return True

def ong_tekshirish(mat, satr, ustun):
    for j in range(ustun + 1, m):
        if mat[satr][j] <= mat[satr][ustun]:
            return False
    return True

k = 0
for i in range(n):
    for j in range(m):
        if (matrisa[i][j] > ustun_yigindi(matrisa, i, j) and
            chap_tekshirish(matrisa, i, j) and
            ong_tekshirish(matrisa, i, j)):
            print(matrisa[i][j])
            k += 1

print("Maxsus elementlar soni:", k)



    