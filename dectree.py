import math


def matchAllCondition(row, arr):
    tambah = 0
    for item in arr:
        a = row[item[0]]
        b = item[1]

        if type(a) is str:
            a = a.lower()

        if type(b) is str:
            b = b.lower()

        if(a == b):
            tambah += 1

    if(tambah == len(arr)):
        return True

    return False


def hitungProbabilitas(data, arr, output="prob", banding=None):
    if banding == 0:
        print("banding adalah 0\ntidak bisa membagi dengan 0")
        return False

    if banding is None:
        banding = len(data)

    # Params
    # arr= [
    #     [idx,key]
    # ]
    # column[idx] == key

    totalMatch = 0
    for row in data:
        isMatch = matchAllCondition(row, arr)

        if(isMatch):
            totalMatch += 1

    if output == "prob":
        return totalMatch/banding
    else:
        return totalMatch


def bagianEntropy(num):
    return (-1 * num * math.log(num, 2))


def entropy(arr):

    jml = 0
    for el in arr:
        jml += el

    tambah = 0
    for x in arr:
        if(x == 0):
            tambah += 0
        else:
            tambah += bagianEntropy(x/jml)

    return tambah


def gainCount(EntropTotal, jmlTotal, arrKlas):

    arrGain = []

    for el in arrKlas:
        tambah = 0
        for x in el[1]:
            tambah += x[0]/jmlTotal*x[1]

        total = EntropTotal-tambah

        arrGain.append([el[0], total])

    return arrGain


def filterDataset(data, arr):
    # Params
    # arr= [
    #     [idx,key]
    # ]
    # column[idx] == key

    filteredDataset = []

    for row in data:
        isMatch = matchAllCondition(row, arr)

        if(isMatch):
            filteredDataset.append(row)

    return filteredDataset


def cariEntropyTiapKlas(data, arrCheck):
    arrKlas = []

    for row in arrCheck:

        klas = []
        for i in range(0, len(row[2])):

            jmlYes = hitungProbabilitas(data, [
                [row[0], row[2][i]],
                [5, "yes"]
            ], "jumlah")

            jmlNo = hitungProbabilitas(data, [
                [row[0], row[2][i]],
                [5, "no"]
            ], "jumlah")

            jml = jmlYes + jmlNo

            en = entropy([jmlYes, jmlNo])

            klas.append([jml, en])

        arrKlas.append([row[1], klas])

    return arrKlas


def cariEntropyTotal(data):
    # Menghitung entropy total
    jmlYes = hitungProbabilitas(data, [
        [5, "yes"]
    ], "jumlah")

    jmlNo = hitungProbabilitas(data, [
        [5, "no"]
    ], "jumlah")

    jmlTotal = jmlYes+jmlNo

    EntropTotal = entropy([jmlYes, jmlNo])

    return [EntropTotal, jmlTotal]


def cariAttributeDgnGainMax(arr):
    maximal = arr[0]

    for row in arr:
        if(maximal[1] < row[1]):
            maximal = row

    return maximal


def findKlas(key, idx, arrCheck):
    for m in arrCheck:

        if(m[1] == key):

            for i in range(0, len(m[2])):

                if(i == idx):
                    return m[2][i]

def cetakNode(arrKlas, maximal, arrCheck):
    # [ idx , nama, [ child1 , child2, ] ]
    # idx   = index column humadity in datasets
    # nama  = " humadity"
    # child = [
    #     "h",
    #     "entropy"
    # ]

    for i in arrKlas:
        if (i[0] is maximal[0]):
            nama = maximal[0]
            arrChild = []

            for k in range(0, len(i[1])):
                a = i[1][k][1]
                b = findKlas(nama, k, arrCheck)

                arrChild.append([b, a])

            for row in arrCheck:
                if(row[1] == maximal[0]):
                    idx = row[0]

            return [idx, nama, arrChild]


def hitungNode(data, arrCheck):
    # Call Function

    arrKlas = cariEntropyTiapKlas(data, arrCheck)

    a = cariEntropyTotal(data)

    arrGain = gainCount(a[0], a[1], arrKlas)

    maximal = cariAttributeDgnGainMax(arrGain)

    node = cetakNode(arrKlas, maximal, arrCheck)

    # print(node)
    return node


def filterArrCheck(key):
    arrCheckNew = []

    for row in arrCheck:
        if(row[1] != key):
            arrCheckNew.append(row)

    return arrCheckNew


def level(newDatasets, newArrCheck, tadiSudah):
    data = newDatasets
    arrCheck = newArrCheck
    node = hitungNode(data, arrCheck)
    print(node)
    for row in node[2]:

        if(not (row[1] == 0)):
            a = [node[0], row[0]]
            tadiSudah.append(a)

            newDatasets = filterDataset(data, tadiSudah)
            newArrCheck = filterArrCheck(node[1])

    return [newDatasets, newArrCheck, tadiSudah]


# __________________________ MAIN __________________________

# Datasets berdasarkan modul
data = [
    [1, "s", "h", "h", "f", "no"],
    [2, "s", "h", "h", "t", "no"],
    [3, "c", "h", "h", "f", "yes"],
    [4, "r", "m", "h", "f", "yes"],
    [5, "r", "c", "n", "f", "yes"],
    [6, "r", "c", "n", "t", "yes"],
    [7, "c", "c", "n", "t", "yes"],
    [8, "s", "m", "h", "f", "no"],
    [9, "s", "c", "n", "f", "yes"],
    [10, "r", "m", "n", "f", "yes"],
    [11, "s", "m", "n", "t", "yes"],
    [12, "c", "m", "h", "t", "yes"],
    [13, "c", "h", "n", "f", "yes"],
    [14, "r", "m", "h", "t", "no"],
]


# Struktur data dari arrCheck

# [idxInData, "nama_kolom", ["class1" ,"class2", ... ] ]

arrCheck = [
    [1, "outlook",     ["c", "r", "s"]],  # outlook
    [2, "temperature", ["c", "h", "m"]],  # temperature
    [3, "humadity",    ["h", "n", ]],   # humadity
    [4, "windy",       ["f", "t"]],     # windy
]


tadiSudah = []

data, arrCheck, tadiSudah = level(data, arrCheck, tadiSudah)

data, arrCheck, tadiSudah = level(data, arrCheck, tadiSudah)

data, arrCheck, tadiSudah = level(data, arrCheck, tadiSudah)
